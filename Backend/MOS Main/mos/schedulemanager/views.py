from rest_framework import viewsets
from .models import Schedule, ScheduleSet
from .serializers import ScheduleSerializer, ScheduleSetSerializer

from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema

# SCHEDULE VIEWSET
@method_decorator(name='list', decorator=swagger_auto_schema(tags=['Schedule']))
@method_decorator(name='create', decorator=swagger_auto_schema(tags=['Schedule']))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(tags=['Schedule']))
@method_decorator(name='update', decorator=swagger_auto_schema(tags=['Schedule']))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(tags=['Schedule']))
@method_decorator(name='destroy', decorator=swagger_auto_schema(tags=['Schedule']))
class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

# SCHEDULE SET VIEWSET
@method_decorator(name='list', decorator=swagger_auto_schema(tags=['ScheduleSet']))
@method_decorator(name='create', decorator=swagger_auto_schema(tags=['ScheduleSet']))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(tags=['ScheduleSet']))
@method_decorator(name='update', decorator=swagger_auto_schema(tags=['ScheduleSet']))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(tags=['ScheduleSet']))
@method_decorator(name='destroy', decorator=swagger_auto_schema(tags=['ScheduleSet']))
class ScheduleSetViewSet(viewsets.ModelViewSet):
    queryset = ScheduleSet.objects.all()
    serializer_class = ScheduleSetSerializer
