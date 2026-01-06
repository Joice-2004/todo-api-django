from rest_framework.decorators import api_view
from rest_framework.request import Request

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from feature.musicdirector.views import MusicDirectorView
from feature.musicdirector.serializer.request.create_music_director_request import (
    CreateMusicDirectorRequestSerializer
)
from feature.musicdirector.serializer.request.update_music_director_request import (
    UpdateMusicDirectorRequestSerializer
)
from feature.common.utils import Utils




page_num_param = openapi.Parameter(
    "page_num",
    openapi.IN_QUERY,
    description="Page number for pagination",
    type=openapi.TYPE_INTEGER,
    default=1
)

limit_param = openapi.Parameter(
    "limit",
    openapi.IN_QUERY,
    description="Number of records per page",
    type=openapi.TYPE_INTEGER,
    default=10
)

id_param = openapi.Parameter(
    "id",
    openapi.IN_QUERY,
    description="Music Director ID",
    type=openapi.TYPE_INTEGER,
    required=True
)


class MusicDirectorController:
    view = MusicDirectorView()



    @staticmethod
    @swagger_auto_schema(
        method="post",
        operation_summary="Create Music Director",
        operation_description="Create a new music director with basic details",
        request_body=CreateMusicDirectorRequestSerializer,
        responses={
            201: "Music director created successfully",
            400: "Validation error"
        }
    )
    @api_view(["POST"])
    def create(request: Request):
        serializer = CreateMusicDirectorRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        params = serializer.save()
        return MusicDirectorController.view.create(params)



    @staticmethod
    @swagger_auto_schema(
        method="get",
        operation_summary="Get All Music Directors",
        operation_description="Fetch all music directors with pagination support",
        manual_parameters=[page_num_param, limit_param],
        responses={
            200: "Music directors fetched successfully"
        }
    )
    @api_view(["GET"])
    def get_all(request: Request):
        return MusicDirectorController.view.get_all(request)



    @staticmethod
    @swagger_auto_schema(
        method="get",
        operation_summary="Get Music Director By ID",
        operation_description="Fetch details of a music director using ID",
        manual_parameters=[id_param],
        responses={
            200: "Music director fetched successfully",
            404: "Music director not found"
        }
    )
    @api_view(["GET"])
    def get_one(request: Request):
        params = Utils.get_query_params(request)
        return MusicDirectorController.view.get_one(params)



    @staticmethod
    @swagger_auto_schema(
        method="put",
        operation_summary="Update Music Director",
        operation_description="Update an existing music director using ID",
        manual_parameters=[id_param],
        request_body=UpdateMusicDirectorRequestSerializer,
        responses={
            200: "Music director updated successfully",
            404: "Music director not found"
        }
    )
    @api_view(["PUT"])
    def update(request: Request):
        params_qs = Utils.get_query_params(request)
        director_id = params_qs.get("id")

        serializer = UpdateMusicDirectorRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        params = serializer.save()

        return MusicDirectorController.view.update(int(director_id), params)



    @staticmethod
    @swagger_auto_schema(
        method="delete",
        operation_summary="Delete Music Director",
        operation_description="Delete a music director using ID",
        manual_parameters=[id_param],
        responses={
            200: "Music director deleted successfully",
            404: "Music director not found"
        }
    )
    @api_view(["DELETE"])
    def delete(request: Request):
        params = Utils.get_query_params(request)
        return MusicDirectorController.view.delete(int(params.get("id")))
