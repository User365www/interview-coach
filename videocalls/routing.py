from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    # Эта строка - это аналог path() из urls.py, но для WebSocket.
    # Она использует "регулярное выражение", чтобы "вырезать" из URL-адреса
    # уникальный ID комнаты (UUID).
    # Адрес будет выглядеть так: ws://.../ws/videocall/ВАШ_UUID_ЗДЕСЬ/
    re_path(r'ws/videocall/(?P<room_id>[0-9a-f-]+)/$', consumers.VideoCallConsumer.as_asgi()),
]