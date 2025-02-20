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
            'time_tag',
            'task',
            'command',
            'execution_id',
        ]
        # We keep schedule_set read-only since it is provided by the parent serializer.
        extra_kwargs = {'schedule_set': {'read_only': True}}

class ScheduleSetSerializer(serializers.ModelSerializer):
    # Allow writable nested schedules
    schedules = ScheduleSerializer(many=True)
    tasks = serializers.SerializerMethodField()

    class Meta:
        model = ScheduleSet
        fields = [
            'id',
            'schedule_set_id',
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
        instance.schedule_set_id = validated_data.get('schedule_set_id', instance.schedule_set_id)
        instance.description = validated_data.get('description', instance.description)
        instance.save()

        if schedules_data is not None:
            # Create a lookup of existing schedules by id for quick access.
            schedule_mapping = {schedule.id: schedule for schedule in instance.schedules.all()}
            for schedule_data in schedules_data:
                schedule_id = schedule_data.get('id', None)
                if schedule_id and schedule_id in schedule_mapping:
                    # Update the existing schedule.
                    schedule_instance = schedule_mapping[schedule_id]
                    for attr, value in schedule_data.items():
                        setattr(schedule_instance, attr, value)
                    schedule_instance.save()
                else:
                    # Create a new schedule if no id was provided or it wasn't found.
                    Schedule.objects.create(schedule_set=instance, **schedule_data)
            # Optionally, you can remove schedules not included in the payload.
        return instance

    def get_tasks(self, obj):
        """
        Returns unique tasks associated with this ScheduleSet via the Schedule model.
        """
        task_queryset = Task.objects.filter(schedule__schedule_set=obj).distinct()
        return TaskSerializer(task_queryset, many=True).data
