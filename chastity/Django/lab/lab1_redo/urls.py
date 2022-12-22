from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("password_generator/", views.password_generator, name="password_generator")
]