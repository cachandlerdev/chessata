import json
from sqlite3 import IntegrityError
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import secrets
from channels.auth import login

from . import models


class ClientConsumer(WebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_id_length = 12
        self.user_id = ""
        self.color = ""

    def connect(self):
        """Connects a new websocket client to the server and performs init 
        logic."""
        self.game_code = self.scope['url_route']['kwargs']['game_code']
        self.game_group_code = f'game_{self.game_code}'

        self.username = self.scope['url_route']['kwargs']['username']
        self.user_id = secrets.token_urlsafe(self.user_id_length)
        
        if self.game_code == "" or self.username == "":
            self.close()

        self._add_user_to_match()
        self.accept()

        self.send(text_data=json.dumps({
            "type": "init",
            "user_id": self.user_id,
            "role": "player",
        }))
    
    
    def _add_user_to_match(self):
        """Updates the ChessUser database to keep track of this user."""
        # TODO: Handle spectators 

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.game_group_code,
            self.channel_name
        )

        other_users = models.ChessUser.objects.filter(game_code=self.game_code)
        num_of_other_players = len(other_users.exclude(color="").all())
        
        # TODO: Add an option to select the player color
        
        if num_of_other_players == 0:
            self.color = "white"
        elif num_of_other_players == 1:
            self.color = "black"
        
        # Save to database
        self.chess_user = models.ChessUser(user_id=self.user_id, 
                                    username=self.username,
                                    game_code=self.game_code,
                                    color=self.color)
        try:
            self.chess_user.save()
        except IntegrityError as e:
            print(str(e))
            self.close()
        
        # Inform other clients
        role = "player" if self.color != "" else "spectator"
        self._broadcast_to_lobby({
            "type": "join",
            "user_id": self.user_id,
            "username": self.username,
            "role": role
        })
    
    
    def disconnect(self, close_code):
        """Runs when the websocket client disconnects from the server."""
        if self.user_id != "":
            all_users = models.ChessUser.objects.filter(game_code=self.game_code)
            other_users = all_users.exclude(pk=self.user_id)

            num_of_other_players = len(other_users.exclude(color="").all())
            if num_of_other_players == 0:
                # Kick out all spectators
                self._broadcast_to_lobby({
                    "type": "close",
                    "message": "Both players have left the match."
                })
            else:
                # Check if he was a player or a spectator.
                if self.color == "":
                    self._broadcast_to_lobby({
                        "type": "leave",
                        "user_id": self.user_id,
                        "username": self.username,
                        "role": "spectator",
                    })
                else:
                    self._broadcast_to_lobby({
                        "type": "leave",
                        "user_id": self.user_id,
                        "username": self.username,
                        "role": "player",
                    })
                    self._handle_player_leaving()

        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.game_group_code,
            self.channel_name
        )
        self.chess_user.delete()
    
    
    def _handle_player_leaving(self):
        """Gets called when this player leaves the match. We check whether 
        the match was over, and send an End of Game message packet if it 
        was still in progress."""
        # TODO
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
    