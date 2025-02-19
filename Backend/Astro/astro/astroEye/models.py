from django.db import models

class CommandResource(models.Model):
    command_id = models.CharField(max_length=20, unique=True)  # e.g., "CMD001"
    power = models.IntegerField()  # Power requirement in watts
    storage = models.IntegerField()  # Storage requirement in MB

    def __str__(self):
        return f"{self.command_id} - Power: {self.power}W, Storage: {self.storage}MB"