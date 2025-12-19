from django.urls import path
from feature.songsapp.controller import SongController
urlpatterns = [
    path("create/",SongController.create),
    path("", SongController.get_all),
    path("get/",SongController.get_one),
    path("update/",SongController.update),
    path("delete/",SongController.delete),
]
