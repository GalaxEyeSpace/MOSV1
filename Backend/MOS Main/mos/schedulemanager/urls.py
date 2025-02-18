from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ScheduleViewSet, ScheduleSetViewSet

router = DefaultRouter()
router.register(r'schedules', ScheduleViewSet, basename='schedules')
router.register(r'schedule-sets', ScheduleSetViewSet, basename='schedule-sets')

urlpatterns = [
    path('', include(router.urls)),
]
