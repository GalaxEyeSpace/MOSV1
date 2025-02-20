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
    list_display = ('task_id', 'priority', 'category', 'status')
    inlines = [TimeSlotInline, TaskCommandInline]
    search_fields = ('task_id', 'category', 'status')


@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ('task', 'start', 'end')

@admin.register(TaskCommand)
class TaskCommandAdmin(admin.ModelAdmin):
    list_display = ('task', 'command', 'time_offset')
    search_fields = ('task__task_id', 'command__command_id')

