from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    """
    Provides GET, POST, PUT, PATCH, DELETE for Task (plus nested timeslots & commands).
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
