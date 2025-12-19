from rest_framework import serializers

class TodoResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    description = serializers.CharField()
    is_completed = serializers.BooleanField()

