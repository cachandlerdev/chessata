import json
from sqlite3 import IntegrityError
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from channels.auth import login

from . import lobby_manager
from . import chess_manager


class ClientConsumer(WebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_id = ""
        self.color = ""
        self.role = ""

    def connect(self):
        """Connects a new websocket client to the server and performs init 
        logic."""
        self.game_code = self.scope['url_route']['kwargs']['game_code']
        self.username = self.scope['url_route']['kwargs']['username']
        self.game_group_code = f'game_{self.game_code}'

        self.user_id, self.role = lobby_manager.create_user(self.game_code, 
                                                            self.username)
        if self.user_id == "" or self.role == "":
            self.close()
        
        if not chess_manager.does_match_exist(self.game_code):
            chess_manager.create_new_match(self.game_code)

        self._add_client_to_match()
        self.accept()

        self.send(text_data=json.dumps({
            "type": "init",
            "user_id": self.user_id,
            "role": "player",
        }))
    
    
    def _add_client_to_match(self):
        """Updates the ChessUser database to keep track of this user."""
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.game_group_code,
            self.channel_name
        )
        
        try:
            self.color = lobby_manager.add_user_to_match(self.user_id, 
                                                         self.game_code, 
                                                         self.username)
        except IntegrityError as e:
            print(str(e))
            self.close()
        
        num_of_players, num_of_spectators = lobby_manager.get_num_of_users(self.game_code)
        
        # Inform other clients
        self._broadcast_to_lobby({
            "type": "receive.user.join",
            "user_id": self.user_id,
            "username": self.username,
            "role": self.role,
            "num_of_players": num_of_players,
            "num_of_spectators": num_of_spectators,
        })
        
        # If this was the 2nd player to join, start the match. 
        num_of_players, _ = lobby_manager.get_num_of_users(self.game_code)
        if self.role == "player" and num_of_players == 2:
            self._start_game()
            self._send_game_state()
    
    
    def receive_user_join(self, event):
        """Tells this client that a new user has joined."""
        user_id = event['user_id']
        username = event['username']
        role = event['role']
        num_of_players = event['num_of_players']
        num_of_spectators = event['num_of_spectators']
        self.send(text_data=json.dumps({
            "type": "join",
            "user_id": user_id,
            "username": username,
            "role": role,
            "num_of_players": num_of_players,
            "num_of_spectators": num_of_spectators,
        }))
    
    
    def _start_game(self):
        """Sends a 'start game' message packet to all lobby members."""
        self._broadcast_to_lobby({
            "type": "receive.start.game",
            "message": "Begin match."
        })
    
    
    def receive_start_game(self, event):
        """Receives a request to begin the match from the server, and informs 
        this client accordingly."""
        self.send(text_data=json.dumps({
            "type": "start",
            "color": self.color,
        }))
    
    
    def disconnect(self, close_code):
        """Runs when the websocket client disconnects from the server."""
        lobby_manager.disconnect_user(self.user_id)
        
        if self.role == "player":
            is_lobby_closed = self._on_player_leave()
        else:
            is_lobby_closed = False
        
        if is_lobby_closed:
            # Kick out all spectators
            self._broadcast_to_lobby({
                "type": "receive.close",
                "message": "Both players have left the match."
            })
        else:
            self._broadcast_to_lobby({
                "type": "receive.leave",
                "user_id": self.user_id,
                "username": self.username,
                "role": self.role,
            })

        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.game_group_code,
            self.channel_name
        )
    
    
    def receive_close(self, event):
        """Tells the client websocket that the lobby has been closed because both
        players have left the match."""
        message = event["message"]
        self.send(text_data=json.dumps({
            "type": "close",
            "message": message,
        }))


    def receive_leave(self, event):
        """Tells the client websocket that a user has left the match."""
        user_id = event["user_id"]
        username = event["username"]
        role = event["role"]
        self.send(text_data=json.dumps({
            "type": "leave",
            "user_id": user_id,
            "username": username,
            "role": role,
        }))
    
    
    def _on_player_leave(self):
        """Runs when this player leaves the match. We check whether the match
        was over and send an End of Game message packet if it wasn't.
        Returns true if the lobby was closed, and false otherwise."""
        if chess_manager.is_match_in_progress(self.game_code):
            self._send_surrender()
        
        return lobby_manager.close_if_all_players_left(self.game_code)
    
    
    def _send_surrender(self):
        """Used in cases where a match is ended prematurely due to a surrender or
        a disconnect."""
        other_player = lobby_manager.get_other_player(self.user_id, self.game_code)
        if other_player is None:
            print("Other player somehow disconnected without ending the match.")
            return

        winning_color = other_player.color
        match_state = f"{winning_color} win"
        chess_manager.end_match(self.game_code, match_state)

        game_data = chess_manager.get_game_state(self.game_code)
        self._broadcast_to_lobby({
            "type": "receive.game.state",
            "state": game_data,
        })
    
    
    def receive(self, text_data):
        """Receives a message from the client attached to this consumer."""
        # Receive message from WebSocket
        try:
            text_data_json = json.loads(text_data)
        except ValueError:
            message = "Response could not be parsed."
            self._send_error(message, 400)
            return
        
        match text_data_json["type"]:
            case "chat":
                self._send_chat_message(text_data_json)
            case "move":
                self._send_move(text_data_json)
            case _:
                # Unsupported move
                self._send_error("Unsupported move type", 400)
    
    
    def _send_chat_message(self, data):
        """Parses this chat JSON object and sends a message to all users in the 
        lobby.""" 
        text = data["message"]
        self._broadcast_to_lobby({
            "type": "receive.chat.message",
            "username": self.username,
            "message": text
        })
    
    
    def _send_move(self, data):
        """Parses this move JSON object and tries to make the corresponding move
        on the backend. If successful, we send out a game state packet to all
        users in the lobby. If not, we send back an error packet to the 
        sender."""
        start = data["start"]
        end = data["end"]
        try:
            promotion = data["promotion"]
        except KeyError:
            promotion = "queen"
        success, fail_reason = chess_manager.make_match_move(self.game_code, 
                                                             start, 
                                                             end, 
                                                             self.user_id, 
                                                             promotion)
        if success:
            self._send_game_state()
        else:
            self._send_error(fail_reason, 405)
    
    
    def _send_game_state(self):
        """Reads the state of the game associated with this game code from the 
        database and sends it to all users in the lobby."""
        game_data = chess_manager.get_game_state(self.game_code)
        
        if game_data == "":
            self._send_error("Game does not exist.", 404)
            return

        self._broadcast_to_lobby({
            "type": "receive.game.state",
            "state": game_data,
        })


    def receive_game_state(self, event):
        """Receives the state of a game from the room group and sends it to the
        client websocket."""
        # We manually read the values to simplify things on the client's end and
        # just send "your turn": true/false.
        game_state = event['state']

        player_turn_id = game_state['player_turn_id']
        is_your_turn = (player_turn_id == self.user_id)

        match_state = game_state['match_state']
        board = game_state['board']
        allow_en_passant = game_state['allow_en_passant']
        has_king_moved = game_state['has_king_moved']
        has_rook_moved = game_state['has_rook_moved']
        self.send(text_data=json.dumps({
            "type": "game_state",
            "state": {
                "your_turn": is_your_turn,
                "match_state": match_state,
                "board": board,
                "allow_en_passant": allow_en_passant,
                "has_king_moved": has_king_moved,
                "has_rook_moved": has_rook_moved,
            }
        }))
    
    
    def _send_error(self, message, status_code):
        """Sends back an error message to the client."""
        self.send(text_data=json.dumps({
            "type": "error",
            "status_code": status_code,
            "message": message
            }))
        
    
    def receive_chat_message(self, event):
        """Receives a chat message from the room group and sends it to the 
        client websocket."""
        # Receive message from room group
        username = event['username']
        message = event['message']
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            "type": "chat",
            "username": username,
            "message": message,
        }))
    
    
    def _broadcast_to_lobby(self, data, game_code=""):
        """Broadcasts the following JSON message packet to all users in the 
        lobby. If no game code is specified, we default to the current 
        consumer's channel layer."""
        if game_code == "":
            game_code = self.game_group_code

        async_to_sync(self.channel_layer.group_send)(game_code, data)
    