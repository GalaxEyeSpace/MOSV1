from django.http import JsonResponse
from .services import fetch_satellite_data, get_passages, fetch_available_passes, book_passage_service, store_passages
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

    # Store or update passages in DB
    store_passages(data)

    # Retrieve and return all stored passages
    all_passages = SatellitePassage.objects.all().values()

    return JsonResponse(list(all_passages), safe=False)

import logging
logger = logging.getLogger(__name__)

def get_available_passes_view(request):
    # Log request method and parameters
    logger.warning(f"Request Method: {request.method}")
    logger.warning(f"GET Params: {request.GET}")  # Log query params
    logger.warning(f"POST Data: {request.POST}")  # If it's a POST request
    logger.warning(f"Request Headers: {dict(request.headers)}") 

    data = fetch_available_passes()

    if "error" in data:
        logger.error(f"Error fetching available passes: {data['error']}")
        return JsonResponse({"error": data["error"]}, status=400)

    return JsonResponse(data, safe=False)

from django.views.decorators.csrf import csrf_exempt

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