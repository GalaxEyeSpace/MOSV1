from django.urls import path
from .views import propagate_orbit_view, multiple_propagate_orbit_view

urlpatterns = [
   path('propagate-orbit/', propagate_orbit_view, name='propagate_orbit'),
   path('multi-propagate/', multiple_propagate_orbit_view, name='multi_propagate'),
   # path('resource/', resource_estimation_view, name='resource_estimation')
]