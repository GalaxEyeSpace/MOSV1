from django.contrib import admin
from .models import Velocity, Storage, Power, Position

# Register the models to be visible in the admin interface

admin.site.register(Velocity)
admin.site.register(Storage)
admin.site.register(Power)
admin.site.register(Position)