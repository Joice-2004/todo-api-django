from django.urls import path
from todoapp.views import TodoView

urlpatterns = [
    path('create/', TodoView.as_view()),
    path('get/<int:pk>/', TodoView.as_view()),
    path('get_all/', TodoView.as_view()),
    path('update/<int:pk>/', TodoView.as_view()),
    path('delete/<int:pk>/', TodoView.as_view()),
]
