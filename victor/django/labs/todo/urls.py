from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('save', views.save_todo, name="save_todo")
]