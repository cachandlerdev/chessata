import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import secrets
from channels.auth import login


class ClientConsumer(WebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_id_length = 12
        self.user_id = ""

    def connect(self):
        self.game_code = self.scope['url_route']['kwargs']['game_code']
        self.game_group_code = f'chat_{self.game_code}'

        self.username = self.scope['url_route']['kwargs']['username']
        self.user_id = secrets.token_urlsafe(self.user_id_length)

        # TODO: Handle spectators 

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.game_group_code,
            self.channel_name
        )
        self.accept()

        self.send(text_data=json.dumps({
            "type": "init",
            "user_id": self.user_id,
            "role": "player",
        }))
    
    
    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.game_group_code,
            self.channel_name
        )
    
    
    def receive(self, text_data):
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
        
        # Check whether this user is associated with an id.
        #user = self.scope["user"]
        #async_to_sync(login)(self.scope, user)
        #self.scope["session"].save

        text = text_data_json['text']
        sender = text_data_json['sender']
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.game_group_code,
            {
                'type': 'chat_message',
                'message': text,
                'sender': sender
            }
        )
        
    
    
    def chat_message(self, event):
        # Receive message from room group
        text = event['message']
        sender = event['sender']
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'text': text,
            'sender': sender
        }))
    