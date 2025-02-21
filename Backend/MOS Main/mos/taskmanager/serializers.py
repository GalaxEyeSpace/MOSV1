from rest_framework import serializers
from django.shortcuts import get_object_or_404
from .models import Task, TimeSlot, TaskCommand
from Utility.models import Command

class TimeSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlot
        fields = ['id', 'start', 'end']

class TaskCommandSerializer(serializers.ModelSerializer):
    command_id = serializers.CharField(write_only=True)
    
    class Meta:
        model = TaskCommand
        fields = ['id', 'time_offset', 'parameters', 'command_id', 'execution_time', 'status']

    def create(self, validated_data):
        command_id = validated_data.pop('command_id', None)
        task = validated_data.get('task')
        command = get_object_or_404(Command, command_id=command_id)
        return TaskCommand.objects.create(task=task, command=command, **validated_data)
    
    def update(self, instance, validated_data):
        instance.time_offset = validated_data.get('time_offset', instance.time_offset)
        instance.parameters = validated_data.get('parameters', instance.parameters)
        instance.status = validated_data.get('status', instance.status)
        instance.execution_time = validated_data.get('execution_time', instance.execution_time)
        instance.save()
        return instance

class TaskSerializer(serializers.ModelSerializer):
    time_slots = TimeSlotSerializer(many=True, required=False)
    task_commands = TaskCommandSerializer(many=True, required=False)

    class Meta:
        model = Task
        fields = ['id', 'task_name_optional', 'priority', 'category', 'status', 'duration', 'execution_time', 'time_slots', 'task_commands']

    def create(self, validated_data):
        time_slots_data = validated_data.pop('time_slots', [])
        task_commands_data = validated_data.pop('task_commands', [])
        
        task = Task.objects.create(**validated_data)

        for ts_data in time_slots_data:
            TimeSlot.objects.create(task=task, **ts_data)

        for tc_data in task_commands_data:
            command_id = tc_data.pop('command_id')
            command = get_object_or_404(Command, command_id=command_id)
            TaskCommand.objects.create(task=task, command=command, **tc_data)

        return task

    def update(self, instance, validated_data):
        instance.task_name_optional = validated_data.get('task_name_optional', instance.task_name_optional)
        instance.priority = validated_data.get('priority', instance.priority)
        instance.category = validated_data.get('category', instance.category)
        instance.status = validated_data.get('status', instance.status)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.execution_time = validated_data.get('execution_time', instance.execution_time)
        instance.save()
        return instance
