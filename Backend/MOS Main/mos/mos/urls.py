from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('leaf/', include('leaf.urls')),
    path('telemetry/', include('telemetry.urls'))
]
