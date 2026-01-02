from rest_framework import serializers
from feature.musicdirector.dataclass.music_director_request import CreateMusicDirectorRequest

class CreateMusicDirectorRequestSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    age = serializers.IntegerField()
    experience = serializers.IntegerField()
    famous_album = serializers.CharField(max_length=255)
    is_active = serializers.BooleanField(required=False)

    def create(self, validated_data):
        return CreateMusicDirectorRequest(**validated_data)
