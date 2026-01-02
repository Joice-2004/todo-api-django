from rest_framework import serializers

class SongResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    singers = serializers.CharField()
    is_active = serializers.BooleanField()
    music_director = serializers.SerializerMethodField()

    def get_music_director(self, obj):
        if obj.music_director:
            return {
                "id": obj.music_director.id,
                "name": obj.music_director.name
            }
        return None
