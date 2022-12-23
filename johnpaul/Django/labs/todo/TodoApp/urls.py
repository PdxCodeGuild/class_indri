from django.urls import path
from . import views

urlpatterns = [
    path('', views.TodoApp, name='home'),
    path('save/', views.SaveToDoItem, name='saved_items'),
]