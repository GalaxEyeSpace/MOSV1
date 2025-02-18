from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommandViewSet

router = DefaultRouter()
router.register(r'commands', CommandViewSet, basename='commands')

urlpatterns = [
    path('', include(router.urls)),
]
