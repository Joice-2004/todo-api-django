from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "todo"

    @staticmethod
    def create(title: str, description: str = "", is_completed: bool = False):
        todo = Todo.objects.create(
            title=title,
            description=description,
            is_completed=is_completed
        )
        return todo



    @staticmethod
    def get_all(params=None):
        return Todo.objects.all()


    @staticmethod
    def get_one(todo_id: int):
        return Todo.objects.filter(id=todo_id).first()

    @staticmethod
    def update(todo_id: int, title: str = None, description: str = None, is_completed: bool = None):
        todo = Todo.objects.filter(id=todo_id).first()
        if not todo:
            return None

        if title is not None:
            todo.title = title

        if description is not None:
            todo.description = description

        if is_completed is not None:
            todo.is_completed = is_completed

        todo.save()
        return todo

    @staticmethod
    def delete_one(todo_id: int):
        todo = Todo.objects.filter(id=todo_id).first()
        if not todo:
            return False

        todo.delete()
        return True
