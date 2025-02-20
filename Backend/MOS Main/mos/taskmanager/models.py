from django.db import models
from django.db.models import JSONField   # or from django.db.models import JSONField (Django 3.1+)

class Task(models.Model):
    """
    A Task can have multiple time slots and multiple commands.
    """
    task_id = models.CharField(max_length=50, unique=True, db_index=True)
    priority = models.IntegerField(default=3)
    category = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=50, default='pending')
    duration = models.IntegerField(default=0, help_text="Duration in minutes")

    def __str__(self):
        return f"Task {self.task_id} (Priority: {self.priority})"


class TimeSlot(models.Model):
    """
    A single time slot for a given Task.
    """
    task = models.ForeignKey(Task, related_name='time_slots', on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __str__(self):
        return f"TimeSlot for {self.task.task_id} from {self.start} to {self.end}"


class TaskCommand(models.Model):
    """
    An intermediate model that links a Task to a Command with additional fields.
    """
    task = models.ForeignKey(Task, related_name='task_commands', on_delete=models.CASCADE)
    command = models.ForeignKey('Utility.Command', related_name='command_in_tasks', on_delete=models.CASCADE)
    time_offset = models.FloatField(default=0.0, help_text="Time offset in seconds")
    parameters = JSONField(blank=True, null=True)

    def __str__(self):
        return f"{self.command.command} in {self.task.task_id})"
