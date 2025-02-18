from django.db import models

class Command(models.Model):
    """
    Represents a base command object with no additional time/parameter info attached yet.
    """
    command_id = models.CharField(max_length=50, unique=True, db_index=True)
    name = models.CharField(max_length=100)
    subsystem = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.command_id} - {self.name}"
