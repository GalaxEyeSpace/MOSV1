from rest_framework import serializers
from .models import Schedule, ScheduleSet

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = [
            'id',
            'schedule_set',
            'execution_id',
            'time_tag',
            'task',
            'command'
        ]

class ScheduleSetSerializer(serializers.ModelSerializer):
    schedules = ScheduleSerializer(many=True, read_only=True)

    class Meta:
        model = ScheduleSet
        fields = [
            'id',
            'schedule_set_id',
            'description',
            'schedules'
        ]
