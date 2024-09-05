from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/api/game_code/(?P<game_code>\w+)/$", consumers.TextRoomConsumer.as_asgi()),
]

# The websocket will open at 127.0.0.1:8000/ws/api/game_code/<game_code>/
application = ProtocolTypeRouter({
    'websocket':
        URLRouter(
            websocket_urlpatterns
        )
})