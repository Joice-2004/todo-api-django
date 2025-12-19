from rest_framework import serializers
from feature.songsapp.dataclass.songs_request import CreateSongRequest

class CreateSongRequestSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    singers = serializers.CharField(max_length=255)
    is_active = serializers.BooleanField(required=False)

    def create(self, validated_data):
        return CreateSongRequest(**validated_data)
