from django.db import models
from django.db.models import JSONField   # or from django.db.models import JSONField (Django 3.1+)
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from datetime import timedelta


class Task(models.Model):
    """
    A Task can have multiple time slots and multiple commands.
    """
    task_name_optional = models.CharField(max_length=50, blank=True, null=True)
    priority = models.IntegerField(default=3)
    category = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=50, default='pending')
    duration = models.IntegerField(default=0, help_text="Duration in minutes")
    execution_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Task {self.id} (Priority: {self.priority})"


class TimeSlot(models.Model):
    """
    A single time slot for a given Task.
    """
    task = models.ForeignKey(Task, related_name='time_slots', on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __str__(self):
        return f"TimeSlot for {self.task.id} from {self.start} to {self.end}"


class TaskCommand(models.Model):
    """
    An intermediate model that links a Task to a Command with additional fields.
    """
    task = models.ForeignKey(Task, related_name='task_commands', on_delete=models.CASCADE)
    command = models.ForeignKey('Utility.Command', related_name='command_in_tasks', on_delete=models.CASCADE)
    time_offset = models.FloatField(default=0.0, help_text="Time offset in seconds")
    parameters = JSONField(blank=True, null=True)
    execution_time = models.DateTimeField(blank=True, null=True, help_text="Calculated execution time")
    status = models.CharField(max_length=50, default='pending')

    def save(self, *args, **kwargs):
        if self.task.execution_time:
            self.execution_time = self.task.execution_time + timedelta(seconds=self.time_offset)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.command.name} in {self.task.id})"


@receiver(post_save, sender=Task)
def update_task_commands_execution_time(sender, instance, **kwargs):
    """
    Signal to update execution_time for all TaskCommands when Task execution_time changes.
    """
    if instance.execution_time:
        for task_command in instance.task_commands.all():
            task_command.execution_time = instance.execution_time + timedelta(seconds=task_command.time_offset)
            task_command.save(update_fields=['execution_time'])
