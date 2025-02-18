from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('leaf/', include('leaf.urls')),
    path('api/utility/', include('Utility.urls')),
    path('api/task-planner/', include('taskmanager.urls')),
    path('api/schedule-planner/', include('schedulemanager.urls')),
]

