import os
import django

# Ensure settings are properly configured before anything else
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'simulator.settings')  # Update with your actual project name
django.setup()  # Initialize Django before importing anything else

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from sim.routing import websocket_urlpatterns  # Import WebSocket routes

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(websocket_urlpatterns)
    ),
})