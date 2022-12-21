from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path('rps/', views.rps, name='rps'),
    path("rps/<str:user_choice>/", views.rps_game, name="rps_game")
]