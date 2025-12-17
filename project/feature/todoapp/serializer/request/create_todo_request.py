from rest_framework import serializers
from project.feature.todoapp.dataclass.todo_request import CreateTodoRequest

class CreateTodoRequestSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    is_completed = serializers.BooleanField(required=False)

    def create(self, validated_data):
        return CreateTodoRequest(**validated_data)


