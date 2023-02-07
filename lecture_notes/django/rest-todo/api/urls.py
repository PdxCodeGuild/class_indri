from django.urls import path
from .views import ListTodos, ListCompletedTodos, DetailTodo

urlpatterns = [
    path("", ListTodos.as_view()),
    path("completed/", ListCompletedTodos.as_view()),
    path("<int:pk>/", DetailTodo.as_view())
]
