from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from todoapp.views import TodoView
from todoapp.serializer.request.create_todo_request import CreateTodoRequestSerializer
from todoapp.serializer.request.update_todo_request import UpdateTodoRequestSerializer
from todoapp.serializer.response.todo_response import TodoResponseSerializer


view = TodoView()


@api_view(["POST"])
def create(request: Request):
    serializer = CreateTodoRequestSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    params = serializer.save()

    todo = view.create(params)

    return Response(TodoResponseSerializer(todo).data)


@api_view(["GET"])
def get_all(request: Request):
    todos = view.get_all()
    return Response(TodoResponseSerializer(todos, many=True).data)


@api_view(["GET"])
def get_one(request: Request, id: int):
    todo = view.get_one(id)
    if not todo:
        return Response({"error": "Not found"}, status=404)
    return Response(TodoResponseSerializer(todo).data)


@api_view(["PUT"])
def update(request: Request, id: int):
    serializer = UpdateTodoRequestSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    params = serializer.save()

    todo = view.update(id, params)
    if not todo:
        return Response({"error": "Not found"}, status=404)

    return Response(TodoResponseSerializer(todo).data)


@api_view(["DELETE"])
def delete(request: Request, id: int):
    success = view.delete(id)
    return Response({"deleted": success})
