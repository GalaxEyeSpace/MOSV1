from django.contrib import admin
from .models import Schedule, ScheduleSet

class ScheduleInline(admin.TabularInline):
    model = Schedule
    extra = 1

@admin.register(ScheduleSet)
class ScheduleSetAdmin(admin.ModelAdmin):
    inlines = [ScheduleInline]


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('schedule_set', 'task','execution_id', 'execution_time')
    list_filter = ('schedule_set', 'task')
    search_fields = ('execution_id', 'task__task_id', 'command__command_id')
