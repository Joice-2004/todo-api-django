from rest_framework import serializers
from project.feature.songsapp.dataclass.songs_request import UpdateSongRequest

class UpdateSongRequestSerializer(serializers.Serializer):
    name = serializers.CharField(required=False, allow_blank=True)
    description = serializers.CharField(required=False, allow_blank=True)
    singers = serializers.CharField(required=False, allow_blank=True)
    is_active = serializers.BooleanField(required=False)

    def create(self, validated_data):
        return UpdateSongRequest(**validated_data)
