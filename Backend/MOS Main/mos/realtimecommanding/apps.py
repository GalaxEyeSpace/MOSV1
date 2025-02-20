from django.apps import AppConfig
from .mqttservice import start_mqtt

class MqttAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'realtimecommanding'  # Adjust according to your Django app name

    def ready(self):
        """Start MQTT on Django startup."""
        start_mqtt()