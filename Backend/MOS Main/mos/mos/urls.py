from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
# Configure drf-yasg to generate your OpenAPI schema

# 1) Define the patterns you WANT included in swagger:
swagger_urlpatterns = [
    path('api/utility/', include('Utility.urls')),
    path('api/task-planner/', include('taskmanager.urls')),
    path('api/schedule-planner/', include('schedulemanager.urls')),
    path('telemetry/', include('telemetry.urls')),
    # ^^^ only these two sets of endpoints => only these two models
]

# 2) Create the schema_view with those patterns:
schema_view = get_schema_view(
    openapi.Info(
        title="Mission Operation API",
        default_version='v1',
        description="MOS MVP Functionality",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    patterns=swagger_urlpatterns,  # <--- This is critical
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('leaf/', include('leaf.urls')),
    path('telemetry/', include('telemetry.urls')),
    path('api/utility/', include('Utility.urls')),
    path('api/task-planner/', include('taskmanager.urls')),
    path('api/schedule-planner/', include('schedulemanager.urls')),

    # Swagger and Redoc Endpoints:
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/',
         schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/',
         schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

