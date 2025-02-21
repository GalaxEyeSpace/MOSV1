from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from .filters import TaskFilter
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg import openapi

# Task VIEWSET
@method_decorator(name='list', decorator=swagger_auto_schema(
    tags=['Task'],
    manual_parameters=[
        openapi.Parameter('start_time', openapi.IN_QUERY, description="Filter by start time", type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
        openapi.Parameter('end_time', openapi.IN_QUERY, description="Filter by end time", type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
        openapi.Parameter('status', openapi.IN_QUERY, description="Filter by status", type=openapi.TYPE_STRING),
        openapi.Parameter('category', openapi.IN_QUERY, description="Filter by category", type=openapi.TYPE_STRING),
        openapi.Parameter('priority', openapi.IN_QUERY, description="Filter by priority", type=openapi.TYPE_INTEGER),
    ]
))
@method_decorator(name='create', decorator=swagger_auto_schema(tags=['Task']))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(tags=['Task']))
@method_decorator(name='update', decorator=swagger_auto_schema(tags=['Task']))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(tags=['Task']))
@method_decorator(name='destroy', decorator=swagger_auto_schema(tags=['Task']))
class TaskViewSet(viewsets.ModelViewSet):
    """
    Provides GET, POST, PUT, PATCH, DELETE for Task (plus nested timeslots & commands).
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TaskFilter
