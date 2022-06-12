from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path("<str:title>", consumers.ChatConsumer.as_asgi()),
]