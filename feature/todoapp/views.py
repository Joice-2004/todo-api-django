# Create your views here.
from rest_framework.response import Response
from feature.todoapp.serializer.response.todo_response import TodoResponseSerializer
from feature.todoapp.model.models import Todo
from feature.common.utils import Utils
from rest_framework import status
from django.core.paginator import Paginator



class TodoView:
    def create(self, params):
        todo = Todo.create(
            title=params.title,
            description=params.description,
            is_completed=params.is_completed
        )
        data = TodoResponseSerializer(todo).data
        return Response(Utils.success_response("Todo created successfully", data),status=status.HTTP_201_CREATED)

    def get_all(self, request):
        params = Utils.get_query_params(request)

        page_num = int(params.get("page_num", 1))
        limit = int(params.get("limit", 10))

        qs = Todo.get_all()  # FULL queryset

        pages = Paginator(qs, limit)

        if pages.num_pages < page_num:
            return Response(
                status=status.HTTP_200_OK,
                data=Utils.error_response("Invalid page", "Page number exceeded")
            )

        page = pages.page(page_num)

        data = TodoResponseSerializer(page.object_list, many=True).data

        data = Utils.add_page_parameter(
            final_data=data,
            page_num=page_num,
            total_page=pages.num_pages,
            total_count=pages.count,
            present_url=request.get_full_path(),
            next_page_required=pages.num_pages != page_num
        )

        return Response(
            status=status.HTTP_200_OK,
            data=Utils.success_response("Data fetched successfully", data)
        )

    def get_one(self, params: dict):
        todo_id = params.get("id")

        if not todo_id:
            return Response(
                Utils.error_response("Validation error", "id is required"),status=status.HTTP_400_BAD_REQUEST)

        todo = Todo.get_one(int(todo_id))
        if not todo:
            return Response(
                Utils.error_response("Todo not found", f"id {todo_id} does not exist"),status=status.HTTP_200_OK)

        data = TodoResponseSerializer(todo).data
        return Response(Utils.success_response("Data fetched successfully", data),status=status.HTTP_200_OK)

    def update(self, todo_id, params):
        todo = Todo.update(
            todo_id,
            title=params.title,
            description=params.description,
            is_completed=params.is_completed
        )
        if not todo:
            return Response(Utils.error_response("Todo not found", f"id {todo_id} does not exist"),status=status.HTTP_200_OK)
        data = TodoResponseSerializer(todo).data
        return Response(Utils.success_response("Todo updated successfully", data),status=status.HTTP_200_OK)

    def delete(self, todo_id: int):
        success = Todo.delete_one(todo_id)
        if not success:
            return Response(Utils.error_response("Todo not found", f"id {todo_id} does not exist"),status=status.HTTP_200_OK)
        return Response(Utils.success_response("Todo deleted successfully"),status=status.HTTP_200_OK)
