# Create your views here.
from rest_framework.response import Response
from project.feature.todoapp.serializer.response.todo_response import TodoResponseSerializer
from project.feature.todoapp.model.models import Todo
from project.feature.utils.utils import Utils



class TodoView:
    def create(self, params):
        todo = Todo.create(
            title=params.title,
            description=params.description,
            is_completed=params.is_completed
        )
        data = TodoResponseSerializer(todo).data
        return Response(Utils.success_response("Todo created successfully", data))


    def get_all(self, params=None):
        todos = Todo.get_all(params)
        data = TodoResponseSerializer(todos, many=True).data
        return Response(Utils.success_response("Data fetched successfully", data))

    def get_one(self, params: dict):
        todo_id = params.get("id")

        if not todo_id:
            return Response(
                Utils.error_response("Validation error", "id is required"),
                status=400
            )

        todo = Todo.get_one(int(todo_id))
        if not todo:
            return Response(
                Utils.error_response("Todo not found", f"id {todo_id} does not exist"),
                status=404
            )

        data = TodoResponseSerializer(todo).data
        return Response(Utils.success_response("Data fetched successfully", data))

    def update(self, todo_id, params):
        todo = Todo.update(
            todo_id,
            title=params.title,
            description=params.description,
            is_completed=params.is_completed
        )
        if not todo:
            return Response(Utils.error_response("Todo not found", f"id {todo_id} does not exist"), status=404)
        data = TodoResponseSerializer(todo).data
        return Response(Utils.success_response("Todo updated successfully", data))

    def delete(self, todo_id: int):
        success = Todo.delete_one(todo_id)
        if not success:
            return Response(Utils.error_response("Todo not found", f"id {todo_id} does not exist"), status=404)
        return Response(Utils.success_response("Todo deleted successfully"))
