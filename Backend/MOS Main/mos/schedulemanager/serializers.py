from rest_framework import serializers
from .models import Schedule, ScheduleSet
from taskmanager.serializers import TaskSerializer
from taskmanager.models import Task

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = [
            'id',
            'schedule_set',
            'task',
            'execution_id',
            'execution_time',
        ]
        extra_kwargs = {'schedule_set': {'read_only': True}}

    def update(self, instance, validated_data):
        instance.task = validated_data.get('task', instance.task)
        instance.execution_id = validated_data.get('execution_id', instance.execution_id)
        instance.execution_time = validated_data.get('execution_time', instance.execution_time)
        instance.save()
        return instance

class ScheduleSetSerializer(serializers.ModelSerializer):
    schedules = ScheduleSerializer(many=True)
    tasks = serializers.SerializerMethodField()

    class Meta:
        model = ScheduleSet
        fields = [
            'id',
            'description',
            'schedules',
            'tasks',
        ]

    def create(self, validated_data):
        schedules_data = validated_data.pop('schedules', [])
        schedule_set = ScheduleSet.objects.create(**validated_data)
        for schedule_data in schedules_data:
            Schedule.objects.create(schedule_set=schedule_set, **schedule_data)
        return schedule_set

    def update(self, instance, validated_data):
        schedules_data = validated_data.pop('schedules', None)
        instance.description = validated_data.get('description', instance.description)
        instance.save()

        if schedules_data is not None:
            schedule_mapping = {schedule.id: schedule for schedule in instance.schedules.all()}
            for schedule_data in schedules_data:
                schedule_id = schedule_data.get('id', None)
                if schedule_id and schedule_id in schedule_mapping:
                    schedule_instance = schedule_mapping[schedule_id]
                    for attr, value in schedule_data.items():
                        setattr(schedule_instance, attr, value)
                    schedule_instance.save()
                else:
                    Schedule.objects.create(schedule_set=instance, **schedule_data)
        return instance

    def get_tasks(self, obj):
        task_queryset = Task.objects.filter(schedule__schedule_set=obj).distinct()
        return TaskSerializer(task_queryset, many=True).data
