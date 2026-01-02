from feature.musicdirector.model.models import MusicDirector
from feature.common.utils import Utils
from rest_framework import status
from rest_framework.response import Response
from django.core.paginator import Paginator
from feature.musicdirector.serializer.response.music_director_response import (
    MusicDirectorResponseSerializer
)

class MusicDirectorView:

    def create(self, params):
        director = MusicDirector.create(
            name=params.name,
            age=params.age,
            experience=params.experience,
            famous_album=params.famous_album,
            is_active=params.is_active
        )
        serializer = MusicDirectorResponseSerializer(director)

        return Response(
            status=status.HTTP_201_CREATED,
            data=Utils.success_response(
                "Music director created successfully",
                serializer.data
            )
        )

    def get_all(self, request):
        params = Utils.get_query_params(request)
        page_num = int(params.get("page_num", 1))
        limit = int(params.get("limit", 10))

        qs = MusicDirector.get_all()
        pages = Paginator(qs, limit)

        if pages.num_pages < page_num:
            raise ValueError("Page number exceeded")

        page_data = pages.page(page_num)
        serializer = MusicDirectorResponseSerializer(
            page_data.object_list,
            many=True
        )

        final_data = Utils.add_page_parameter(
            final_data=serializer.data,
            page_num=page_num,
            total_page=pages.num_pages,
            total_count=pages.count,
            present_url=request.get_full_path(),
            next_page_required=True if pages.num_pages != page_num else False
        )

        return Response(
            status=status.HTTP_200_OK,
            data=Utils.success_response(
                "Data fetched successfully",
                final_data
            )
        )

    def get_one(self, params):
        director = MusicDirector.get_one(int(params.get("id")))

        if not director:
            return Response(
                Utils.error_response("Not Found", "Music director not found"),
                status=status.HTTP_200_OK
            )

        serializer = MusicDirectorResponseSerializer(director)

        return Response(
            Utils.success_response(
                "Data fetched successfully",
                serializer.data
            ),
            status=status.HTTP_200_OK
        )

    def update(self, director_id, params):
        director = MusicDirector.update(
            director_id,
            name=params.name,
            age=params.age,
            experience=params.experience,
            famous_album=params.famous_album,
            is_active=params.is_active
        )

        if not director:
            return Response(
                Utils.error_response("Not Found", "Music director not found"),
                status=status.HTTP_200_OK
            )

        serializer = MusicDirectorResponseSerializer(director)

        return Response(
            Utils.success_response(
                "Music director updated successfully",
                serializer.data
            ),
            status=status.HTTP_200_OK
        )

    def delete(self, director_id):
        success = MusicDirector.delete_one(director_id)

        if not success:
            return Response(
                Utils.error_response("Not Found", "Music director not found"),
                status=status.HTTP_200_OK
            )

        return Response(
            Utils.success_response(
                "Music director deleted successfully"
            ),
            status=status.HTTP_200_OK
        )
