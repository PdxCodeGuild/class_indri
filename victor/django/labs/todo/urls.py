from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('save', views.save_todo, name="save_todo"),
    path('delete/<int:id>', views.delete_todo, name="delete_todo"),
    path('complete/<int:id>', views.complete_todo, name='complete_todo'),
]