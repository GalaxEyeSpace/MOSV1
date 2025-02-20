from django.contrib import admin
from .models import SatellitePassage, PassageBooking  # Import your model

# Register the model in the admin panel
@admin.register(SatellitePassage)
class SatellitePassageAdmin(admin.ModelAdmin):
    list_display = ("passage_id", "satellite_id", "ground_station_id", "aos", "los", "passage_status")
    search_fields = ("passage_id", "satellite_id", "ground_station_id")
    list_filter = ("passage_status", "policy_type", "bandwidth_type")
    ordering = ("-aos",)  # Show the latest passages first

@admin.register(PassageBooking)
class PassageBookingAdmin(admin.ModelAdmin):
    list_display = ("candidateID", "passageID", "AOS", "LOS")  # Fields shown in list view
    search_fields = ("candidateID", "passageID")  # Enables search functionality
    list_filter = ("AOS", "LOS")  # Adds filters on the right panel
    ordering = ("AOS",)  # Orders entries by AOS time
