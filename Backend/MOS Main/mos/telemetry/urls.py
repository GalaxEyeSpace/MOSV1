from django.urls import path
from .views import get_tm_data  # Import the API view

urlpatterns = [
    path("get-data/", get_tm_data),  # Add the API endpoint
]