from rest_framework.decorators import api_view
from rest_framework.request import Request
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from feature.todoapp.views import TodoView
from feature.todoapp.serializer.request.create_todo_request import CreateTodoRequestSerializer
from feature.todoapp.serializer.request.update_todo_request import UpdateTodoRequestSerializer
from feature.common.utils import Utils


class TodoController:
    view = TodoView()


    @staticmethod
    @swagger_auto_schema(
        method="post",
        operation_summary="Create Todo",
        operation_description="Create a new todo item",
        request_body=CreateTodoRequestSerializer,
        responses={201: openapi.Response("Todo created successfully")}
    )
    @api_view(["POST"])
    def create(request: Request):
        serializer = CreateTodoRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        params = serializer.save()
        return TodoController.view.create(params)


    @staticmethod
    @swagger_auto_schema(
        method="get",
        operation_summary="Get all todos",
        operation_description="Fetch all todo items with pagination",
        manual_parameters=[
            openapi.Parameter("page_num", openapi.IN_QUERY, type=openapi.TYPE_INTEGER),
            openapi.Parameter("limit", openapi.IN_QUERY, type=openapi.TYPE_INTEGER),
        ],
        responses={200: openapi.Response("Todo list")}
    )
    @api_view(["GET"])
    def get_all(request: Request):
        return TodoController.view.get_all(request)


    @staticmethod
    @swagger_auto_schema(
        method="get",
        operation_summary="Get todo by ID",
        operation_description="Fetch a single todo using ID",
        manual_parameters=[
            openapi.Parameter("id", openapi.IN_QUERY, type=openapi.TYPE_INTEGER, required=True)
        ],
        responses={200: openapi.Response("Todo details")}
    )
    @api_view(["GET"])
    def get_one(request: Request):
        params = Utils.get_query_params(request)
        return TodoController.view.get_one(params)


    @staticmethod
    @swagger_auto_schema(
        method="put",
        operation_summary="Update todo",
        operation_description="Update todo details using ID",
        request_body=UpdateTodoRequestSerializer,
        manual_parameters=[
            openapi.Parameter("id", openapi.IN_QUERY, type=openapi.TYPE_INTEGER, required=True)
        ],
        responses={200: openapi.Response("Todo updated successfully")}
    )
    @api_view(["PUT"])
    def update(request: Request):
        params_qs = Utils.get_query_params(request)
        todo_id = params_qs.get("id")

        serializer = UpdateTodoRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        params = serializer.save()

        return TodoController.view.update(int(todo_id), params)


    @staticmethod
    @swagger_auto_schema(
        method="delete",
        operation_summary="Delete todo",
        operation_description="Delete a todo using ID",
        manual_parameters=[
            openapi.Parameter("id", openapi.IN_QUERY, type=openapi.TYPE_INTEGER, required=True)
        ],
        responses={200: openapi.Response("Todo deleted successfully")}
    )
    @api_view(["DELETE"])
    def delete(request: Request):
        params = Utils.get_query_params(request)
        todo_id = params.get("id")
        return TodoController.view.delete(int(todo_id))
