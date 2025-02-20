import base64
import json
import requests
from datetime import datetime, timedelta
from django.conf import settings
from .models import SatellitePassage
from django.http import JsonResponse
from django.utils.dateparse import parse_datetime

# Configuration (make sure to add these in your settings)
USERNAME = settings.EXTERNAL_API_SETTINGS['USERNAME']
PASSWORD = settings.EXTERNAL_API_SETTINGS['PASSWORD']
TOKEN_URL = settings.EXTERNAL_API_SETTINGS['TOKEN_URL']

# Global variables for token management
ACCESS_TOKEN = None
TOKEN_EXPIRY = None  # Stores the expiry time of the token

def get_access_token():
    """Fetch a new access token if expired or not available."""
    global ACCESS_TOKEN, TOKEN_EXPIRY

    # Check if token is still valid
    if ACCESS_TOKEN and TOKEN_EXPIRY and datetime.now() < TOKEN_EXPIRY:
        return ACCESS_TOKEN  # Return existing token if still valid

    try:
        # Generate Base64-encoded authentication string
        auth_string = f"{USERNAME}:{PASSWORD}"
        auth_encoded = base64.b64encode(auth_string.encode()).decode()

        headers = {
            "Authorization": f"Basic {auth_encoded}",
            "Content-Type": "application/x-www-form-urlencoded",
        }
        data = {"grant_type": "client_credentials"}

        # Fetch new token
        response = requests.post(TOKEN_URL, headers=headers, data=data)
        response.raise_for_status()
        token_data = response.json()
        
        # Extract token and set expiry time (12 hours from now)
        ACCESS_TOKEN = token_data.get("access_token")
        TOKEN_EXPIRY = datetime.now() + timedelta(hours=12)

        return ACCESS_TOKEN
    except requests.RequestException as e:
        print(f"Error fetching access token: {str(e)}")
        return None

def get_auth_headers():
    """Generate authentication headers with the access token."""
    token = get_access_token()
    if not token:
        return {"error": "Authentication failed"}
    
    return {
        "Accept": "application/json",
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }

def fetch_satellite_data():
    """Fetch satellite data from the external API."""
    url = "https://apiv2.sandbox.leaf.space/satellites/e0e000c339ebce2829051c8a95513458"
    headers = get_auth_headers()
    
    # If authentication failed, return the error response
    if "error" in headers:
        return {"error": headers["error"]}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()  # Return the data from the API
    except requests.RequestException as e:
        return {"error": f"Failed to fetch satellite data: {str(e)}"}
    

# Fetch Available Passages
def get_passages():
    url = "https://apiv2.sandbox.leaf.space/passages?satellite_id=e0e000c339ebce2829051c8a95513458"
    headers = get_auth_headers()
    if "error" in headers:
        return {"error": headers["error"]}

    try:
        response = requests.get(url, headers=headers)
        # print(response.data)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Failed to fetch schedule data: {str(e)}"}
    
def store_passages(data):
    """
    Stores or updates passage records in the database.
    """
    if "response" not in data:
        return {"error": "Invalid response format"}

    passages = data["response"]  # Extract passage list

    for passage in passages:
        passage_id = passage["passageID"]

        # Convert string timestamps to datetime objects
        aos = parse_datetime(passage["AOS"])
        tca = parse_datetime(passage["TCA"])
        los = parse_datetime(passage["LOS"])

        # Update if passage exists, otherwise create a new entry
        SatellitePassage.objects.update_or_create(
            passage_id=passage_id,
            defaults={
                "satellite_id": passage["satelliteID"],
                "ground_station_id": passage["groundStationID"],
                "max_elevation": passage["maxElevation"],
                "passage_status": passage["passageStatus"],
                "keyhole_bypass": passage["keyholeBypass"] == "true",
                "source": passage["source"],
                "aos": aos,
                "tca": tca,
                "los": los,
                "passage_result_id": passage["passageResultID"],
                "policy_type": passage["policyType"],
                "bandwidth_type": passage["bandwidthType"],
            },
        )

    
def fetch_available_passes():
    url = "https://apiv2.sandbox.leaf.space/passages/candidates?satellite_id=e0e000c339ebce2829051c8a95513458&booking_status=available"
    headers = get_auth_headers()
    if "error" in headers:
        return {"error": headers["error"]}

    try:
        response = requests.get(url, headers=headers)
        # print(response)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Failed to fetch data: {str(e)}"}

def book_passage_service(request_body):
    """Handles passage booking by forwarding request to external API and saving to DB."""
    headers = get_auth_headers()

    try:
        # ✅ Ensure request body is not empty
        if not request_body:
            return {"error": "Empty request body", "status": 400}

        data = json.loads(request_body)  # Parse JSON payload

        # ✅ Ensure at least one candidateID exists
        if not isinstance(data, dict) or not data:
            return {"error": "Invalid request format", "status": 400}

        # ✅ Extract first candidateID and passage details
        candidateID, passage_info = next(iter(data.items()))
        policyType = passage_info.get("policyType")
        start = passage_info.get("start")
        end = passage_info.get("end")

        # ✅ Validate required fields
        if not all([candidateID, policyType, start, end]):
            return {"error": "Missing required fields: candidateID, policyType, start, end", "status": 400}

        # ✅ Convert start & end time to datetime format
        start_dt = datetime.strptime(start, "%Y-%m-%dT%H:%M:%SZ")
        end_dt = datetime.strptime(end, "%Y-%m-%dT%H:%M:%SZ")

        # ✅ API Request Setup
        url = "https://apiv2.sandbox.leaf.space/passages/candidates/book?allow_overlap=false"
        api_payload = {
            candidateID: {
                "policyType": policyType,
                "start": start,
                "end": end,
            }
        }

        response = requests.post(url, headers=headers, json=api_payload)
        response.raise_for_status()  # Raises HTTP error if response is not 200

        # ✅ Handle API Response
        booking_response = response.json()
        if "response" not in booking_response or not booking_response["response"]:
            return {"error": "Booking failed, no passage data found.", "status": 400}

        return {"data": booking_response, "status": 200}

    except json.JSONDecodeError:
        return {"error": "Invalid JSON format in request", "status": 400}
    except requests.RequestException as e:
        return {"error": f"Failed to book passage: {str(e)}", "status": 500}
    except Exception as e:
        return {"error": f"Internal Server Error: {str(e)}", "status": 500}
    

from django.views.decorators.csrf import csrf_exempt
from .models import PassageBooking

@csrf_exempt  # ❗️If using Django's CSRF protection, ensure frontend handles CSRF tokens properly
def book_passage(request):
    """
    Handles booking a passage via the external API and stores the booking in the database.
    """
    headers = get_auth_headers()

    if request.method != "POST":
        return JsonResponse({"error": "Invalid request method"}, status=405)

    try:
        # ✅ Ensure request body is not empty
        if not request.body:
            return JsonResponse({"error": "Empty request body"}, status=400)

        data = json.loads(request.body)  # Parse JSON payload

        # ✅ Ensure at least one candidateID exists
        if not isinstance(data, dict) or not data:
            return JsonResponse({"error": "Invalid request format"}, status=400)

        # ✅ Extract first candidateID
        candidateID, passage_info = next(iter(data.items()))

        # ✅ Extract passage details
        policyType = passage_info.get("policyType")
        start = passage_info.get("start")
        end = passage_info.get("end")

        # ✅ Validate required fields
        if not all([candidateID, policyType, start, end]):
            return JsonResponse(
                {"error": "Missing required fields: candidateID, policyType, start, end"},
                status=400,
            )

        # ✅ Convert start & end time to datetime format
        start_dt = datetime.strptime(start, "%Y-%m-%dT%H:%M:%SZ")
        end_dt = datetime.strptime(end, "%Y-%m-%dT%H:%M:%SZ")

        # ✅ Forward request to external API
        url = "https://apiv2.sandbox.leaf.space/passages/candidates/book?allow_overlap=false"
        api_payload = {
            candidateID: {
                "policyType": policyType,
                "start": start,
                "end": end,
            }
        }

        response = requests.post(url, headers=headers, json=api_payload)
        response.raise_for_status()  # Raises HTTP error if response is not 200

        # ✅ Handle API Response
        booking_response = response.json()

        # ✅ Ensure response has expected structure
        if "response" not in booking_response or not booking_response["response"]:
            return JsonResponse({"error": "Booking failed, no passage data found."}, status=400)

        passage_data = booking_response["response"][0].get("passage", {})

        # ✅ Save to Django database
        PassageBooking.objects.update_or_create(
            candidateID=candidateID,
            defaults={
                "passageID": passage_data.get("passageID", ""),
                "AOS": start_dt,
                "LOS": end_dt,
            },
        )

        return JsonResponse(booking_response, safe=False)

    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON format in request"}, status=400)
    except requests.RequestException as e:
        return JsonResponse({"error": f"Failed to book passage: {str(e)}"}, status=500)
    except Exception as e:
        return JsonResponse({"error": f"Internal Server Error: {str(e)}"}, status=500)