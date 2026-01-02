from rest_framework.decorators import api_view
from rest_framework.request import Request

from feature.musicdirector.views import MusicDirectorView
from feature.musicdirector.serializer.request.create_music_director_request import CreateMusicDirectorRequestSerializer
from feature.musicdirector.serializer.request.update_music_director_request import UpdateMusicDirectorRequestSerializer
from feature.common.utils import Utils


class MusicDirectorController:
    view = MusicDirectorView()

    @staticmethod
    @api_view(["POST"])
    def create(request: Request):
        serializer = CreateMusicDirectorRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        params = serializer.save()
        return MusicDirectorController.view.create(params)

    @staticmethod
    @api_view(["GET"])
    def get_all(request):
        return MusicDirectorController.view.get_all(request)

    @staticmethod
    @api_view(["GET"])
    def get_one(request: Request):
        params = Utils.get_query_params(request)
        return MusicDirectorController.view.get_one(params)

    @staticmethod
    @api_view(["PUT"])
    def update(request: Request):
        params_qs = Utils.get_query_params(request)
        director_id = params_qs.get("id")

        serializer = UpdateMusicDirectorRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        params = serializer.save()

        return MusicDirectorController.view.update(int(director_id), params)

    @staticmethod
    @api_view(["DELETE"])
    def delete(request: Request):
        params = Utils.get_query_params(request)
        return MusicDirectorController.view.delete(int(params.get("id")))

