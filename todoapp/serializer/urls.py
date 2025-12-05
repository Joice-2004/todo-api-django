from django.urls import path, include
from todoapp.serializer.controller import urlpatterns as todo_urls

urlpatterns = [
    path('todo/', include(todo_urls)),
]
