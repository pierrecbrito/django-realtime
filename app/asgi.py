"""
ASGI config for app project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
from chat.routing import websocket_urlpatterns
from django.urls import path
from chat import consumers

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

application = get_asgi_application()

application = ProtocolTypeRouter({
    "http": application,
    "websocket":  AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                [
                    path("ws/chat/<str:grupo>/", consumers.ChatConsumer.as_asgi()),
                ]
            )
        )
    ),
    # Just HTTP for now. (We can add other protocols later.)
})