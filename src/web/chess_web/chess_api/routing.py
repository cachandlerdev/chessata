from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/api/(?P<game_name>\w+)/$", consumers.TextRoomConsumer.as_asgi()),
]

# The websocket will open at 127.0.0.1:8000/ws/api/<room_name>/
application = ProtocolTypeRouter({
    'websocket':
        URLRouter(
            websocket_urlpatterns
        )
})