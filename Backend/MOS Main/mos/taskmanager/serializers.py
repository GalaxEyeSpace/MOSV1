from rest_framework import serializers
from django.shortcuts import get_object_or_404
from .models import Task, TimeSlot, TaskCommand
from Utility.models import Command

class TimeSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlot
        fields = ['id', 'start', 'end']

class TaskCommandSerializer(serializers.ModelSerializer):
    # We can allow writing by command_id, but read a nested Command if needed
    command_id = serializers.CharField(write_only=True)
    # If you want to display Command info, you can nest it or just show the ID
    # command = CommandSerializer(read_only=True)  # from utility.serializers import CommandSerializer

    class Meta:
        model = TaskCommand
        fields = [
            'id', 'execution_id', 'time_offset', 'parameters',
            'command_id', # or 'command' if you want read-only nested
        ]

    def create(self, validated_data):
        command_id = validated_data.pop('command_id', None)
        task = validated_data.get('task')  # parent must be set by context or a higher-level create
        command = get_object_or_404(Command, command_id=command_id)
        return TaskCommand.objects.create(task=task, command=command, **validated_data)


class TaskSerializer(serializers.ModelSerializer):
    time_slots = TimeSlotSerializer(many=True, required=False)
    task_commands = TaskCommandSerializer(many=True, required=False)

    class Meta:
        model = Task
        fields = [
            'id', 'task_id', 'priority', 'category', 'status',
            'time_slots', 'task_commands',
        ]

    def create(self, validated_data):
        time_slots_data = validated_data.pop('time_slots', [])
        task_commands_data = validated_data.pop('task_commands', [])
        
        task = Task.objects.create(**validated_data)

        # Create TimeSlots
        for ts_data in time_slots_data:
            TimeSlot.objects.create(task=task, **ts_data)

        # Create TaskCommands
        for tc_data in task_commands_data:
            command_id = tc_data.pop('command_id')
            command = get_object_or_404(Command, command_id=command_id)
            TaskCommand.objects.create(task=task, command=command, **tc_data)

        return task

    def update(self, instance, validated_data):
        # Simple update: we only update top-level fields
        instance.priority = validated_data.get('priority', instance.priority)
        instance.category = validated_data.get('category', instance.category)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        # For a full nested update of TimeSlots/TaskCommands, handle them similarly
        return instance
