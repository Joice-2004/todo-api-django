from django.shortcuts import render

# Create your views here.
from todoapp.model.models import Todo

class TodoView:

    def create(self, params):
        todo = Todo.create(
            title=params.title,
            description=params.description,
            is_completed=params.is_completed
        )
        return todo

    def get_all(self):
        return Todo.get_all()

    def get_one(self, todo_id: int):
        return Todo.get_one(todo_id)

    def update(self, todo_id, params):
        return Todo.update(
            todo_id,
            title=params.title,
            description=params.description,
            is_completed=params.is_completed
        )

    def delete(self, todo_id: int):
        return Todo.delete_one(todo_id)
