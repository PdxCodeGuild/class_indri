from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("compose/", views.compose, name="compose"),
    path("edit/", views.edit, name="edit"),
]
