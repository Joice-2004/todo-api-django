from django.urls import path
from todoapp.todo_controller import (
    create, get_all, get_one, update, delete
)

urlpatterns = [
    path("create/", create),
    path("all/", get_all),
    path("get/<int:id>/", get_one),
    path("update/<int:id>/", update),
    path("delete/<int:id>/", delete),
]

