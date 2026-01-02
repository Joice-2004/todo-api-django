from rest_framework.response import Response
from feature.songsapp.model.models import Song
from feature.songsapp.serializer.response.song_response import SongResponseSerializer
from feature.common.utils import Utils
from rest_framework import status
from rest_framework.request import Request
from django.core.paginator import Paginator
from feature.musicdirector.model.models import MusicDirector


class SongView:

    def create(self, params):
        director = MusicDirector.objects.filter(
            id=params.music_director_id
        ).first()

        if not director:
            return Response(
                Utils.error_response("Invalid director", "Music director not found"),
                status=status.HTTP_400_BAD_REQUEST
            )

        song = Song.create(
            name=params.name,
            description=params.description,
            singers=params.singers,
            is_active=params.is_active,
            music_director = director
        )
        data = SongResponseSerializer(song).data
        return Response(status=status.HTTP_201_CREATED,
            data=Utils.success_response("Song created successfully", data),

        )
    def get_all(self, request: Request):
        params = Utils.get_query_params(request)
        page_num = int(params.get("page_num", 1))
        limit = int(params.get("limit", 10))

        qs = Song.get_all()

        pages = Paginator(qs, limit)
        if pages.num_pages < page_num:
            raise ValueError("Page number exceeded")

        page_data = pages.page(page_num)
        serialized_data = SongResponseSerializer(page_data.object_list, many=True).data


        final_data = Utils.add_page_parameter(
            final_data=serialized_data,
            page_num=page_num,
            total_page=pages.num_pages,
            total_count=pages.count,
            present_url=request.get_full_path(),
            next_page_required=True if pages.num_pages != page_num else False
        )

        return Response(
            status=status.HTTP_200_OK,
            data=Utils.success_response("Data fetched successfully", final_data)
        )
    def get_one(self, params):
        song_id = params.get("id")
        if not song_id:
            return Response(Utils.error_response("Validation error", "id is required"),status=status.HTTP_400_BAD_REQUEST)

        song = Song.get_one(int(song_id))
        if not song:
            return Response(Utils.error_response("Song not found", f"id {song_id} does not exist"),status=status.HTTP_200_OK)

        data = SongResponseSerializer(song).data
        return Response(Utils.success_response("Data fetched successfully", data),status=status.HTTP_200_OK)

    def update(self, song_id, params):
        song = Song.update(
            song_id,
            name=params.name,
            description=params.description,
            singers=params.singers,
            is_active=params.is_active
        )
        if not song:
            return Response(Utils.error_response("Song not found", f"id {song_id} does not exist"),status=status.HTTP_200_OK)

        data = SongResponseSerializer(song).data
        return Response(Utils.success_response("Song updated successfully", data),status=status.HTTP_200_OK)

    def delete(self, song_id):
        success = Song.delete_one(song_id)
        if not success:
            return Response(Utils.error_response("Song not found", f"id {song_id} does not exist"),status=status.HTTP_200_OK)

        return Response(Utils.success_response("Song deleted successfully"),status=status.HTTP_200_OK)
