from django.contrib import admin
from .models import Schedule, ScheduleSet

class ScheduleInline(admin.TabularInline):
    model = Schedule
    extra = 1

@admin.register(ScheduleSet)
class ScheduleSetAdmin(admin.ModelAdmin):
    list_display = ('schedule_set_id', 'description')
    inlines = [ScheduleInline]
    search_fields = ('schedule_set_id', 'description')

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('schedule_set', 'execution_id', 'time_tag', 'task', 'command')
    list_filter = ('schedule_set', 'time_tag')
    search_fields = ('execution_id', 'task__task_id', 'command__command_id')
