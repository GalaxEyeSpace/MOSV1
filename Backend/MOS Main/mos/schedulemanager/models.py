from django.db import models
from taskmanager.models import TaskCommand

class ScheduleSet(models.Model):
    """
    A grouping or cluster of schedule items.
    """
    schedule_set_id = models.BigIntegerField(unique=True, db_index=True)
    description = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"ScheduleSet {self.schedule_set_id}"

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
    execution_id = models.ForeignKey(TaskCommand, related_name='execution', on_delete=models.CASCADE)
    time_tag = models.DateTimeField()
    task = models.ForeignKey('taskmanager.Task', on_delete=models.CASCADE)
    command = models.ForeignKey('Utility.Command', on_delete=models.CASCADE)

    def __str__(self):
        return f"Schedule - Set: {self.schedule_set_id} | ExecID: {self.execution_id} | {self.time_tag}"
