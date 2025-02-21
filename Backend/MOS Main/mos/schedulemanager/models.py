from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from taskmanager.models import TaskCommand

class ScheduleSet(models.Model):
    """
    A grouping or cluster of schedule items.
    """
    description = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"ScheduleSet {self.description}"

class Schedule(models.Model):
    """
    Each schedule row references:
    - The Task
    - The Command
    - The timeTag when it's scheduled
    - The ExecutionID if needed
    - The ScheduleSet grouping
    """
    schedule_set = models.ForeignKey(ScheduleSet, related_name='schedules', on_delete=models.CASCADE)
    task = models.ForeignKey('taskmanager.Task', on_delete=models.CASCADE)
    execution_id = models.ForeignKey(TaskCommand, related_name='execution', on_delete=models.CASCADE, blank=True, null=True)
    execution_time = models.DateTimeField(blank=True, null=True, help_text="Execution time fetched from TaskCommand")


def save(self, *args, **kwargs):
    if self.execution_id and self.execution_id.execution_time:
        self.execution_time = self.execution_id.execution_time
    super().save(*args, **kwargs)


    def __str__(self):
        return f"Schedule - Set: {self.schedule_set.description} | taskID: {self.task}"

@receiver(post_save, sender=TaskCommand)
def update_schedule_execution_time(sender, instance, **kwargs):
    """
    Signal to update execution_time in Schedule when TaskCommand execution_time changes.
    """
    for schedule in instance.execution.all():
        schedule.execution_time = instance.execution_time
        schedule.save(update_fields=['execution_time'])

