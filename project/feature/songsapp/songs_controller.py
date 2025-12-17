from rest_framework.decorators import api_view
from rest_framework.request import Request

from project.feature.songsapp.views import SongView
from project.feature.songsapp.serializer.request.create_song_request import CreateSongRequestSerializer
from project.feature.songsapp.serializer.request.update_song_request import UpdateSongRequestSerializer
from project.feature.utils.utils import Utils

view = SongView()

@api_view(["POST"])
def create(request: Request):
    serializer = CreateSongRequestSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    params = serializer.save()
    return view.create(params)

@api_view(["GET"])
def get_all(request: Request):
    params = Utils.get_query_params(request)
    return view.get_all(params)

@api_view(["GET"])
def get_one(request: Request):
    params = Utils.get_query_params(request)
    return view.get_one(params)

@api_view(["PUT"])
def update(request: Request):
    params_qs = Utils.get_query_params(request)
    song_id = params_qs.get("id")

    serializer = UpdateSongRequestSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    params = serializer.save()

    return view.update(int(song_id), params)

@api_view(["DELETE"])
def delete(request: Request):
    params = Utils.get_query_params(request)
    song_id = params.get("id")
    return view.delete(int(song_id))
