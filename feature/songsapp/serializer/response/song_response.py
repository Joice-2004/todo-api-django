from rest_framework import serializers

class SongResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    singers = serializers.CharField()
    is_active = serializers.BooleanField()
