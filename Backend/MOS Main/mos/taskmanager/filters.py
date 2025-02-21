import django_filters
from django.db.models import Min, Max
from .models import Task

class TaskFilter(django_filters.FilterSet):
    start_time = django_filters.DateTimeFilter(method='filter_start_time')
    end_time = django_filters.DateTimeFilter(method='filter_end_time')
    status = django_filters.CharFilter(field_name="status", lookup_expr='iexact')
    category = django_filters.CharFilter(field_name="category", lookup_expr='icontains')
    priority = django_filters.NumberFilter(field_name="priority", lookup_expr='exact')

    class Meta:
        model = Task
        fields = ['start_time', 'end_time', 'status', 'category', 'priority']

    def filter_start_time(self, queryset, name, value):
        return queryset.annotate(min_start=Min('time_slots__start')).filter(min_start__gte=value)

    def filter_end_time(self, queryset, name, value):
        return queryset.annotate(max_end=Max('time_slots__end')).filter(max_end__lte=value)
