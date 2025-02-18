import django_filters
from .models import Velocity, Storage, Power, Position, Omega, Attitude, AttErr

class TimeRangeFilter(django_filters.FilterSet):
    start_time = django_filters.DateTimeFilter(field_name="timestep", lookup_expr="gte")
    end_time = django_filters.DateTimeFilter(field_name="timestep", lookup_expr="lte")

    class Meta:
        model = Velocity  # Default model (this will be changed dynamically)
        fields = ["start_time", "end_time"]