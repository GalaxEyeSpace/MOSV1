from django.contrib import admin
from .models import Task, TimeSlot, TaskCommand

class TimeSlotInline(admin.TabularInline):
    model = TimeSlot
    extra = 1

class TaskCommandInline(admin.TabularInline):
    model = TaskCommand
    extra = 1

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_name_optional', 'priority', 'category', 'status', 'duration', 'execution_time')
    inlines = [TimeSlotInline, TaskCommandInline]
    search_fields = ('task_name_optional', 'category', 'status')


@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ('task', 'start', 'end')

@admin.register(TaskCommand)
class TaskCommandAdmin(admin.ModelAdmin):
    list_display = ('task', 'command', 'time_offset', 'execution_time', 'status')
    search_fields = ('task__task_name_optional', 'command__command_id')

