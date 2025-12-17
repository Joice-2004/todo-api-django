from rest_framework.decorators import api_view
from rest_framework.request import Request

from project.feature.todoapp.views import TodoView
from project.feature.todoapp.serializer.request.create_todo_request import CreateTodoRequestSerializer
from project.feature.todoapp.serializer.request.update_todo_request import UpdateTodoRequestSerializer
from project.feature.utils.utils import Utils

view = TodoView()


@api_view(["POST"])
def create(request: Request):
    serializer = CreateTodoRequestSerializer(data=request.data)
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
    todo_id = params_qs.get("id")

    serializer = UpdateTodoRequestSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    params = serializer.save()

    return view.update(int(todo_id), params)


@api_view(["DELETE"])
def delete(request: Request):
    params = Utils.get_query_params(request)
    todo_id = params.get("id")

    return view.delete(int(todo_id))

