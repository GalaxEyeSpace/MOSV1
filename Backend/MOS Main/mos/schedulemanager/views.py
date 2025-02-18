from rest_framework import viewsets
from .models import Schedule, ScheduleSet
from .serializers import ScheduleSerializer, ScheduleSetSerializer

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

class ScheduleSetViewSet(viewsets.ModelViewSet):
    queryset = ScheduleSet.objects.all()
    serializer_class = ScheduleSetSerializer
