import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class TextRoomConsumer(WebsocketConsumer):
    def connect(self):
        self.game_name = self.scope['url_route']['kwargs']['game_name']
        self.game_group_name = f'chat_{self.game_name}'
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.game_group_name,
            self.channel_name
        )
        self.accept()
    
    
    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.game_group_name,
            self.channel_name
        )
    
    
    def receive(self, text_data):
        # Receive message from WebSocket
        text_data_json = json.loads(text_data)
        text = text_data_json['text']
        sender = text_data_json['sender']
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.game_group_name,
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
        