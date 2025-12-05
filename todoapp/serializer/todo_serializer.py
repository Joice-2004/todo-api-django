from rest_framework import serializers
from todoapp.model.todo_model import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
