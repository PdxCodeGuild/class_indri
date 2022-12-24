from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("password_generator/", views.password_generator, name="password_generator"),
    path("rot_cypher/", views.rot, name="rot_cypher"),
    path("rotate/", views.rotate, name="potato"),
    path("unit_converter/", views.unit_converter, name="demonllama"),
    path("rps/", views.rps, name="rps"),
    path("rps/<str:user_choice>/", views.rps_game, name="rps_game")
]