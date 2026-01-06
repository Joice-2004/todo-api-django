from rest_framework.decorators import api_view
from rest_framework.request import Request
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from feature.songsapp.views import SongView
from feature.songsapp.serializer.request.create_song_request import CreateSongRequestSerializer
from feature.songsapp.serializer.request.update_song_request import UpdateSongRequestSerializer
from feature.common.utils import Utils


class SongController:
    view = SongView()


    @staticmethod
    @swagger_auto_schema(
        method="post",
        operation_summary="Create Song",
        operation_description="Create a new song",
        request_body=CreateSongRequestSerializer,
        responses={201: openapi.Response("Song created successfully")}
    )
    @api_view(["POST"])
    def create(request: Request):
        serializer = CreateSongRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        params = serializer.save()
        return SongController.view.create(params)


    @staticmethod
    @swagger_auto_schema(
        method="get",
        operation_summary="Get all songs",
        operation_description="Get paginated list of songs",
        manual_parameters=[
            openapi.Parameter("page_num", openapi.IN_QUERY, type=openapi.TYPE_INTEGER),
            openapi.Parameter("limit", openapi.IN_QUERY, type=openapi.TYPE_INTEGER),
        ],
        responses={200: openapi.Response("Songs list")}
    )
    @api_view(["GET"])
    def get_all(request):
        return SongController.view.get_all(request)


    @staticmethod
    @swagger_auto_schema(
        method="get",
        operation_summary="Get song by ID",
        operation_description="Fetch a single song using ID",
        manual_parameters=[
            openapi.Parameter("id", openapi.IN_QUERY, type=openapi.TYPE_INTEGER, required=True)
        ],
        responses={200: openapi.Response("Song details")}
    )
    @api_view(["GET"])
    def get_one(request: Request):
        params = Utils.get_query_params(request)
        return SongController.view.get_one(params)


    @staticmethod
    @swagger_auto_schema(
        method="put",
        operation_summary="Update song",
        operation_description="Update song details using ID",
        request_body=UpdateSongRequestSerializer,
        manual_parameters=[
            openapi.Parameter("id", openapi.IN_QUERY, type=openapi.TYPE_INTEGER, required=True)
        ],
        responses={200: openapi.Response("Song updated successfully")}
    )
    @api_view(["PUT"])
    def update(request: Request):
        params_qs = Utils.get_query_params(request)
        song_id = params_qs.get("id")

        serializer = UpdateSongRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        params = serializer.save()

        return SongController.view.update(int(song_id), params)


    @staticmethod
    @swagger_auto_schema(
        method="delete",
        operation_summary="Delete song",
        operation_description="Delete a song using ID",
        manual_parameters=[
            openapi.Parameter("id", openapi.IN_QUERY, type=openapi.TYPE_INTEGER, required=True)
        ],
        responses={200: openapi.Response("Song deleted successfully")}
    )
    @api_view(["DELETE"])
    def delete(request: Request):
        params = Utils.get_query_params(request)
        song_id = params.get("id")
        return SongController.view.delete(int(song_id))
