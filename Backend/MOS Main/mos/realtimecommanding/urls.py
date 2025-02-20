from django.urls import path
from .views import mqtt_publish_view

urlpatterns = [
    path("command/", mqtt_publish_view, name="mqtt_publish"),
]
