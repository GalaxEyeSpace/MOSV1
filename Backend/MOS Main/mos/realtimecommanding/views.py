import json
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .mqttservice import publish_and_wait_for_response

@csrf_exempt
def mqtt_publish_view(request):
    try:
        # Parse the incoming request
        data = json.loads(request.body)

        # Extract message and ensure a topic is present
        message = data.get("message")
        topic = settings.MQTT_BROKER["PUBLISH_TOPIC"]

        if not message:
            return JsonResponse({"error": "Message cannot be empty"}, status=400)

        # Publish the message & wait for response
        response = publish_and_wait_for_response(topic, message)

        if response:
            return JsonResponse({"status": "success", "response": response})
        else:
            return JsonResponse({"status": "error", "message": "No response received"})

    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON format"}, status=400)
    
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)