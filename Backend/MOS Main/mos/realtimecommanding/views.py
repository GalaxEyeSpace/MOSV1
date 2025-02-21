import json
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .mqttservice import publish_and_wait_for_response

@csrf_exempt
def mqtt_publish_view(request):
    """API endpoint to publish an MQTT message and return the response."""
    try:
        # Parse request data
        data = json.loads(request.body)

        # Ensure topic is available
        topic = settings.MQTT_BROKER["PUBLISH_TOPIC"]
        if not data:
            return JsonResponse({"error": "Message cannot be empty"}, status=400)

        # Publish message & wait for response
        response = publish_and_wait_for_response(topic, data, timeout=10)

        return JsonResponse({"status": "success", "response": response})

    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON format"}, status=400)
    
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)