from django.contrib import admin
from sim.models import Velocity, Storage, Power, Position  # Import models

# Velocity Model Admin
class VelocityAdmin(admin.ModelAdmin):
    list_display = ("id", "timestep", "x", "y", "z")  # Show these columns
    search_fields = ("timestep",)  # Allow search by timestamp
    list_filter = ("timestep",)  # Add filtering options

# Storage Model Admin
class StorageAdmin(admin.ModelAdmin):
    list_display = ("id", "timestep", "instant_data_gen", "instant_data_down", "ssd_storage", "ssd_capacity")
    search_fields = ("timestep",)
    list_filter = ("timestep",)

# Power Model Admin
class PowerAdmin(admin.ModelAdmin):
    list_display = ("id", "timestep", "net_power", "solar", "storage", "threshold", "power_consumed")
    search_fields = ("timestep",)
    list_filter = ("timestep",)

# Position Model Admin
class PositionAdmin(admin.ModelAdmin):
    list_display = ("id", "timestep", "x", "y", "z")
    search_fields = ("timestep",)
    list_filter = ("timestep",)

# Register the models
admin.site.register(Velocity, VelocityAdmin)
admin.site.register(Storage, StorageAdmin)
admin.site.register(Power, PowerAdmin)
admin.site.register(Position, PositionAdmin)