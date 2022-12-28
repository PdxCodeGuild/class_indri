from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("save/", views.save_url, name="save_url"),
    path('<str:code>/', views.relocate, name="relocate")
]