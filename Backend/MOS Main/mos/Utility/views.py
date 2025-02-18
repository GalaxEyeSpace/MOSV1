from rest_framework import viewsets
from .models import Command
from .serializers import CommandSerializer
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema

# Utility VIEWSET
@method_decorator(name='list', decorator=swagger_auto_schema(tags=['Utility']))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(tags=['Utility']))
class CommandViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Provides GET for Command.
    """
    queryset = Command.objects.all()
    serializer_class = CommandSerializer

