from rest_framework import serializers
from feature.musicdirector.dataclass.music_director_request import UpdateMusicDirectorRequest

class UpdateMusicDirectorRequestSerializer(serializers.Serializer):
    name = serializers.CharField(required=False, allow_blank=True)
    age = serializers.IntegerField(required=False)
    experience = serializers.IntegerField(required=False)
    famous_album = serializers.CharField(required=False, allow_blank=True)
    is_active = serializers.BooleanField(required=False)

    def create(self, validated_data):
        return UpdateMusicDirectorRequest(**validated_data)
