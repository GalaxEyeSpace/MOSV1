from django.contrib import admin
from .models import Command

@admin.register(Command)
class CommandAdmin(admin.ModelAdmin):
    list_display = ('command_id', 'name', 'subsystem')
    search_fields = ('command_id', 'name', 'subsystem')

