from django.http import JsonResponse
from django.apps import apps
import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Velocity, Storage, Power, Position, Omega, Attitude, AttErr
from .filters import TimeRangeFilter

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