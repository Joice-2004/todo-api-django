from django.urls import path
from feature.musicdirector.controller import MusicDirectorController

urlpatterns = [
    path("create/", MusicDirectorController.create),
    path("", MusicDirectorController.get_all),
    path("get/", MusicDirectorController.get_one),
    path("update/", MusicDirectorController.update),
    path("delete/", MusicDirectorController.delete),
]
