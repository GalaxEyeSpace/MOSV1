from django.contrib import admin
from django.apps import apps

# Get all models from the current app
app = apps.get_app_config('telemetry')

# Function to dynamically create a ModelAdmin class with fancy features
def create_fancy_admin_class(model):
    class FancyModelAdmin(admin.ModelAdmin):
        # Display all fields in the list view
        list_display = [field.name for field in model._meta.fields]
        
        # Add search functionality for all CharField and TextField
        search_fields = [field.name for field in model._meta.fields if field.get_internal_type() in ['CharField', 'TextField']]
        
        # Add filters for all ForeignKey, DateField, and BooleanField
        list_filter = [field.name for field in model._meta.fields if field.get_internal_type() in ['ForeignKey', 'DateField', 'DateTimeField', 'BooleanField']]
        
        # Enable ordering by all fields
        ordering = [field.name for field in model._meta.fields]

    return FancyModelAdmin

# Register each model with the admin site, excluding non-managed models
for model_name, model in app.models.items():
    admin.site.register(model, create_fancy_admin_class(model))