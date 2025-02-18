import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mos.settings")

import django
django.setup()

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from telemetry.routing import websocket_urlpatterns  # Import your WebSocket routes
from channels.auth import AuthMiddlewareStack

# Define ASGI application with both HTTP and WebSocket handling
application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # Handle Django admin and API
    "websocket": AuthMiddlewareStack(
        URLRouter(websocket_urlpatterns)  # Handle WebSockets
    ),
})