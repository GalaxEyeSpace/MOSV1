from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .services import propagate_orbit, multistep_propagation, resource_estimation

@csrf_exempt  
def propagate_orbit_view(request):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid request method"}, status=405)

    try:
        request_body = json.loads(request.body)  
        response_data = propagate_orbit(request_body)  # Call propagation service
        return JsonResponse(response_data, safe=False)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON format in request"}, status=400)
    except Exception as e:
        return JsonResponse({"error": f"Internal Server Error: {str(e)}"}, status=500)
    
@csrf_exempt  
def multiple_propagate_orbit_view(request):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid request method"}, status=405)

    try:
        request_body = json.loads(request.body)  
        response_data = multistep_propagation(request_body)  # Call propagation service
        return JsonResponse(response_data, safe=False)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON format in request"}, status=400)
    except Exception as e:
        return JsonResponse({"error": f"Internal Server Error: {str(e)}"}, status=500)
    
@csrf_exempt
def resource_estimation_view(request):
    try:
        request_body = json.loads(request.body)  # Parse JSON request
        response = resource_estimation(request_body)  # Call the service function
        return JsonResponse(response, status=200 if response["status"] == "success" else 400)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
