from django.http import JsonResponse
from django.apps import apps
import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Velocity, Storage, Power, Position, Omega, Attitude, AttErr
from .filters import TimeRangeFilter
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Mapping table names to Django model classes
MODEL_MAPPING = {
    "velocity": Velocity,
    "storage": Storage,
    "power": Power,
    "position": Position,
    "omega": Omega,
    "attitude": Attitude,
    "atterr": AttErr,
}

@swagger_auto_schema(
    method='get',
    manual_parameters=[
        openapi.Parameter(
            'table',
            openapi.IN_QUERY,
            description="Name of the table (velocity, storage, etc.)",
            type=openapi.TYPE_STRING,
            required=True
        ),
        openapi.Parameter(
            'start_time',
            openapi.IN_QUERY,
            description="Start of time range in ISO format (UTC). Example: 2023-02-01T00:00:00Z",
            type=openapi.TYPE_STRING,
            format=openapi.FORMAT_DATETIME,  # <-- Tells Swagger this is date-time
            required=False
        ),
        openapi.Parameter(
            'end_time',
            openapi.IN_QUERY,
            description="End of time range in ISO format (UTC). Example: 2025-02-10T23:59:59Z",
            type=openapi.TYPE_STRING,
            format=openapi.FORMAT_DATETIME,  # <-- Tells Swagger this is date-time
            required=False
        ),
    ],
    responses={
        200: openapi.Response(description="List of matching records or empty list"),
        400: openapi.Response(description="Missing/invalid parameters"),
    }
)
@api_view(["GET"])
def get_tm_data(request):
    """
    Fetch data from a specified table within a time range.
    Example usage:
        /api/get-data/?table=velocity&start_time=2025-02-01T00:00:00Z&end_time=2025-02-10T23:59:59Z
    """
    table_name = request.GET.get("table", None)
    start_time = request.GET.get("start_time", None)
    end_time = request.GET.get("end_time", None)

    if not table_name:
        return Response({"error": "Missing 'table' parameter."}, status=400)

    # Get the corresponding model class from the mapping
    ModelClass = MODEL_MAPPING.get(table_name.lower())
    if not ModelClass:
        return Response({"error": f"Invalid table name '{table_name}'."}, status=400)

    # Apply filters
    filterset = TimeRangeFilter(request.GET, queryset=ModelClass.objects.all())
    if not filterset.is_valid():
        return Response({"error": "Invalid filter parameters."}, status=400)

    # Serialize and return data
    data = filterset.qs.values()  # Converts queryset to JSON
    return Response(list(data))