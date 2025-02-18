from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema

# Task VIEWSET
@method_decorator(name='list', decorator=swagger_auto_schema(tags=['Task']))
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
