from django.urls import path
from .views import TodoView

urlpatterns = [
    path('create/', TodoView.as_view()),
    path('get_all/', TodoView.as_view()),
    path('get/<int:id>/', TodoView.as_view()),
    path('update/<int:id>/', TodoView.as_view()),
    path('delete/<int:id>/', TodoView.as_view()),
]
