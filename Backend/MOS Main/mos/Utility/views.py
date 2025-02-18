from rest_framework import viewsets
from .models import Command
from .serializers import CommandSerializer

class CommandViewSet(viewsets.ModelViewSet):
    """
    Provides GET, POST, PUT, PATCH, DELETE for Command.
    """
    queryset = Command.objects.all()
    serializer_class = CommandSerializer

