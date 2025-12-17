from django.urls import path
from project.feature.todoapp.todo_controller import create, get_all, get_one, update, delete

urlpatterns = [
    path('create/', create, name='todo-create'),     # POST
    path('', get_all, name='todo-get-all'),          # GET all with optional pagination
    path('get/', get_one, name='todo-get-one'),     # GET single, use ?id=1
    path('update/', update, name='todo-update'),    # PUT, use ?id=1
    path('delete/', delete, name='todo-delete'),    # DELETE, use ?id=1
]


