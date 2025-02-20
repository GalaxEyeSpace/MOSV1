from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import CommandResource
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
    
# @csrf_exempt
# def resource_estimation_view(request):
#     try:
#         request_body = json.loads(request.body)  # Parse JSON request
#         response = resource_estimation(request_body)  # Call the service function
#         return JsonResponse(response, status=200 if response["status"] == "success" else 400)

#         try:
#             request_body = json.loads(request.body)  
#             response_data = resource_estimation(request_body)  # Call propagation service
#             return JsonResponse(response_data, safe=False)
#         except json.JSONDecodeError:
#             return JsonResponse({"error": "Invalid JSON format in request"}, status=400)
#         except Exception as e:
#             return JsonResponse({"error": f"Internal Server Error: {str(e)}"}, status=500)
        
@csrf_exempt
def resource_estimation_view(request):
    try:
        request_body = json.loads(request.body)  # Parse JSON request

        print("Processing request body:", request_body)

        current_resources = request_body.get("initial_resources", {})
        command_list = request_body.get("command_ids", [])

        resources_over_time = []

        for command_index, command_id in enumerate(command_list):
            print(f"Processing Command ID {command_id}")

            # Fetch from the database instead of dictionary
            try:
                task_resources = CommandResource.objects.get(command_id=command_id)
            except CommandResource.DoesNotExist:
                return JsonResponse({
                    "status": "failure",
                    "error": f"Invalid Command ID: {command_id}"
                }, status=400)

            power_required = task_resources.power
            storage_required = task_resources.storage

            # Check if resources are sufficient
            if current_resources["power"] >= power_required and current_resources["storage"] >= storage_required:
                current_resources["power"] -= power_required
                current_resources["storage"] -= storage_required

                resources_over_time.append({
                    "command_index": command_index + 1,
                    "command_id": command_id,
                    "remaining_power": current_resources["power"],
                    "remaining_storage": current_resources["storage"],
                })
            else:
                insufficient_resource = "power" if current_resources["power"] < power_required else "storage"
                remaining_resource = current_resources[insufficient_resource]

                return JsonResponse({
                    "status": "failure",
                    "failed_command": command_id,
                    "insufficient_resource": insufficient_resource,
                    "required": getattr(task_resources, insufficient_resource),
                    "remaining": remaining_resource,
                    "remaining_resources": current_resources,
                    "resources_over_time": resources_over_time
                }, status=400)

        return JsonResponse({
            "status": "success",
            "resources_over_time": resources_over_time,
            "final_resources": current_resources
        }, status=200)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
