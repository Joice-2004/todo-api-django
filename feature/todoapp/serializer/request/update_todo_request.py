from rest_framework import serializers
from feature.todoapp.dataclass.todo_request import UpdateTodoRequest

class UpdateTodoRequestSerializer(serializers.Serializer):
    title = serializers.CharField(required=False, allow_blank=True)
    description = serializers.CharField(required=False, allow_blank=True)
    is_completed = serializers.BooleanField(required=False)

    def create(self, validated_data):
        return UpdateTodoRequest(**validated_data)


