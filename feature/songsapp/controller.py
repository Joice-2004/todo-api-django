from rest_framework.decorators import api_view
from rest_framework.request import Request

from feature.songsapp.views import SongView
from feature.songsapp.serializer.request.create_song_request import CreateSongRequestSerializer
from feature.songsapp.serializer.request.update_song_request import UpdateSongRequestSerializer
from feature.common.utils import Utils

class SongController:
    view = SongView()

    @staticmethod
    @api_view(["POST"])
    def create(request: Request):
        serializer = CreateSongRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        params = serializer.save()

        return SongController.view.create(params)

    @staticmethod
    @api_view(["GET"])
    def get_all(request):
        return SongController.view.get_all(request)

    @staticmethod
    @api_view(["GET"])
    def get_one(request: Request):
        params = Utils.get_query_params(request)
        return SongController.view.get_one(params)

    @staticmethod
    @api_view(["PUT"])
    def update(request: Request):
        params_qs = Utils.get_query_params(request)
        song_id = params_qs.get("id")

        serializer = UpdateSongRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        params = serializer.save()
        return SongController.view.update(int(song_id), params)

    @staticmethod
    @api_view(["DELETE"])
    def delete(request: Request):
        params = Utils.get_query_params(request)
        song_id = params.get("id")
        return SongController.view.delete(int(song_id))
