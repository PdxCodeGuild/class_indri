from django.urls import path
from . import views
from .views import TodoCreateView, TodoUpdateView



urlpatterns = [
    path('', views.TodoApp, name='home'),
    path('create/new/', TodoCreateView.as_view(), name='todo_create'),
    path('todo/update', TodoUpdateView.as_view(), name='todo-update'),

    # path('todo/<int:pk>/delete', TodoDeleteView.as_view(), name='todo-delete'),
]