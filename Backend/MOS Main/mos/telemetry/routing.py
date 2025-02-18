from django.urls import re_path
from telemetry.consumers import TelemetryConsumer

websocket_urlpatterns = [
    re_path(r"ws/telemetry/", TelemetryConsumer.as_asgi()),
]