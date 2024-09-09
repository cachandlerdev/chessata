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
        self.user_id_length = 12
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
        # TODO: Handle spectators 

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
        
        # Inform other clients
        self._broadcast_to_lobby({
            "type": "join",
            "user_id": self.user_id,
            "username": self.username,
            "role": self.role
        })
    
    
    def disconnect(self, close_code):
        """Runs when the websocket client disconnects from the server."""
        lobby_manager.disconnect_user(self.user_id)
        
        if self.role == "player":
            self._on_player_leave()
            is_lobby_closed = self._on_player_leave()
        else:
            is_lobby_closed = False
        
        if is_lobby_closed:
            # Kick out all spectators
            self._broadcast_to_lobby({
                "type": "close",
                "message": "Both players have left the match."
            })
        else:
            self._broadcast_to_lobby({
                "type": "leave",
                "user_id": self.user_id,
                "username": self.username,
                "role": self.role,
            })

        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.game_group_code,
            self.channel_name
        )
    
    
    def _on_player_leave(self):
        """Runs when this player leaves the match. We check whether the match
        was over and send an End of Game message packet if it wasn't.
        Returns true if the lobby was closed, and false otherwise."""
        # TODO
        if chess_manager.is_match_in_progress(self.game_code):
            self._end_game("player_left")
        
        return lobby_manager.close_if_all_players_left(self.game_code)
    
    
    def _end_game(self, type):
        """Ends the game for this client's join code. Recognized `type` values
        are 'white_win', 'black_win', 'stalemate', 'surrender', and 'disconnect'."""
        # TODO
        # Send an error/do nothing if the game doesn't exist
        # Match on type
            # White/black win: Get the winning player's ID and color, and send packet
            # Stalemate: Send stalemate packet
            # Surrender: Get remaining player's ID and send surrender packet
            # Disconnect: Get remaining player's ID and send disconnect packet
            
        # Call lobby_manager code that will call chess_manager code and end
        # the match
        pass
        
    
    
    def receive(self, text_data):
        """Receives a message from the client attached to this consumer."""
        # Receive message from WebSocket
        try:
            text_data_json = json.loads(text_data)
        except ValueError:
            self.send(text_data=json.dumps({
                "type": "error",
                "status_code": 406,
                "message": "Response could not be parsed."
                }))
            return
        
        match text_data_json["type"]:
            case "chat":
                self._send_chat_message(text_data_json)
                pass
            case "move":
                # Handle move
                # TODO
                pass
            case _:
                # Unsupported move
                # TODO
                pass
        
        #text = text_data_json['text']
        #sender = text_data_json['sender']

        ## Send message to room group
        #self._broadcast_to_lobby({
        #    'type': 'chat_message',
        #    'message': text,
        #    'sender': sender
        #})
    
    
    def _send_chat_message(self, data):
       """Parses this chat JSON object and sends a message to all users in the 
       lobby.""" 
        
    
    def chat_message(self, event):
        # Receive message from room group
        print(event)
        text = event['message']
        sender = event['sender']
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'text': text,
            'sender': sender
        }))
    
    
    def _broadcast_to_lobby(self, data, game_code=""):
        """Broadcasts the following JSON message packet to all users in the 
        lobby. If no game code is specified, we default to the current 
        consumer's channel layer."""
        if game_code == "":
            game_code = self.game_group_code

        async_to_sync(self.channel_layer.group_send)(game_code, data)
    