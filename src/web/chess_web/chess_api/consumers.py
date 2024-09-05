import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import secrets


class TextRoomConsumer(WebsocketConsumer):
    def connect(self):
        self.game_code = self.scope['url_route']['kwargs']['game_code']
        self.game_group_code = f'chat_{self.game_code}'
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.game_group_code,
            self.channel_name
        )
        self.accept()
    
    
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
        
        
        player_id_length = 12
        player_id = secrets.token_urlsafe(player_id_length)

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
    