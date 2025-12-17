from rest_framework.response import Response
from project.feature.songsapp.model.models import Song
from project.feature.songsapp.serializer.response.song_response import SongResponseSerializer
from project.feature.utils.utils import Utils

class SongView:

    def create(self, params):
        song = Song.create(
            name=params.name,
            description=params.description,
            singers=params.singers,
            is_active=params.is_active
        )
        data = SongResponseSerializer(song).data
        return Response(Utils.success_response("Song created successfully", data))

    def get_all(self, params=None):
        songs = Song.get_all(params)
        data = SongResponseSerializer(songs, many=True).data
        return Response(Utils.success_response("Data fetched successfully", data))

    def get_one(self, params):
        song_id = params.get("id")
        if not song_id:
            return Response(Utils.error_response("Validation error", "id is required"), status=400)

        song = Song.get_one(int(song_id))
        if not song:
            return Response(Utils.error_response("Song not found", f"id {song_id} does not exist"), status=404)

        data = SongResponseSerializer(song).data
        return Response(Utils.success_response("Data fetched successfully", data))

    def update(self, song_id, params):
        song = Song.update(
            song_id,
            name=params.name,
            description=params.description,
            singers=params.singers,
            is_active=params.is_active
        )
        if not song:
            return Response(Utils.error_response("Song not found", f"id {song_id} does not exist"), status=404)

        data = SongResponseSerializer(song).data
        return Response(Utils.success_response("Song updated successfully", data))

    def delete(self, song_id):
        success = Song.delete_one(song_id)
        if not success:
            return Response(Utils.error_response("Song not found", f"id {song_id} does not exist"), status=404)

        return Response(Utils.success_response("Song deleted successfully"))
