from django.http import JsonResponse
from .services import fetch_satellite_data, get_passages, fetch_available_passes, book_passage_service, store_passages, fetch_passage_schedule
from .services import (
    fetch_satellite_data, get_passages, fetch_available_passes, 
    book_passage_service, store_passages
)
from .models import SatellitePassage
from datetime import datetime
import json

def satellite_info_view(request):
    """View for fetching satellite data."""
    data = fetch_satellite_data()
    
    if "error" in data:
        return JsonResponse({"error": data["error"]}, status=500)
    
    return JsonResponse(data, safe=False)

def get_passage_info_view(request):
    """
    Fetches passage info from external API, stores them in the DB, and returns all stored data.
    """
    data = get_passages()

    if "error" in data:
        return JsonResponse({"error": data["error"]}, status=500)

    # Retrieve and return all stored passages
    all_passages = SatellitePassage.objects.all().values()
    return JsonResponse(list(all_passages), safe=False)

@swagger_auto_schema(
    method='get',
    operation_description="Fetch available passes.",
    responses={200: openapi.Response("Available Passes Retrieved Successfully")}
)
@api_view(['GET'])
def get_available_passes_view(request):
    """Fetch available passes from the service."""
    logger.warning(f"Request Method: {request.method}")
    logger.warning(f"GET Params: {request.GET}")
    logger.warning(f"POST Data: {request.POST}")
    logger.warning(f"Request Headers: {dict(request.headers)}")

    data = fetch_available_passes()
    
    if "error" in data:
        logger.error(f"Error fetching available passes: {data['error']}")
        return JsonResponse({"error": data["error"]}, status=400)
    
    return JsonResponse(data, safe=False)

@swagger_auto_schema(
    method='post',
    operation_description="Book a passage.",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'satellite_id': openapi.Schema(type=openapi.TYPE_STRING, description='Satellite ID'),
            'user_id': openapi.Schema(type=openapi.TYPE_STRING, description='User ID'),
            'passage_time': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME, description='Passage Time')
        },
        required=['satellite_id', 'user_id', 'passage_time']
    ),
    responses={
        200: openapi.Response("Passage Booked Successfully"),
        400: openapi.Response("Bad Request")
    }
)
@api_view(['POST'])
@csrf_exempt
def book_passage_view(request):
    """View for booking a passage."""
    if request.method != "POST":
        return JsonResponse({"error": "Invalid request method"}, status=405)
    
    result = book_passage_service(request.body)
    
    if "error" in result:
        logger.error(f"Error booking passage: {result['error']}")
        return JsonResponse({"error": result["error"]}, status=result["status"])
    
    return JsonResponse(result["data"], safe=False, status=result["status"])
