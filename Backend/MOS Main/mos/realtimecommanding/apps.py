from django.apps import AppConfig
import os

class MqttConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "realtimecommanding"

    def ready(self):
        if os.environ.get("RUN_MAIN") == "true":  # Ensures MQTT starts only once
            from .mqttservice import start_mqtt
            start_mqtt()