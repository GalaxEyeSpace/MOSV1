from django.contrib import admin
from .models import UplinkMessage, DownlinkMessage

@admin.register(UplinkMessage)
class UplinkMessageAdmin(admin.ModelAdmin):
    list_display = ("timestamp", "payload")
    search_fields = ("payload",)

@admin.register(DownlinkMessage)
class DownlinkMessageAdmin(admin.ModelAdmin):
    list_display = ("timestamp", "payload")
    # search_fields = ("payload",)