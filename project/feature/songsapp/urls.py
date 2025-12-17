from django.urls import path
from project.feature.songsapp.songs_controller import (
    create, get_all, get_one, update, delete
)

urlpatterns = [
    path("create/", create),
    path("", get_all),
    path("get/", get_one),
    path("update/", update),
    path("delete/", delete),
]
