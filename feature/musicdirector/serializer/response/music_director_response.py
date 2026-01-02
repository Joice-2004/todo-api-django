from rest_framework import serializers

class MusicDirectorResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    age = serializers.IntegerField()
    experience = serializers.IntegerField()
    famous_album = serializers.CharField()
    is_active = serializers.BooleanField()
