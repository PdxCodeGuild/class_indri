from django.urls import path
from . import views

# URL Conf
urlpatterns = [
    path("", views.index, name="home"),
    path('password_generator/', views.password_generator, name='password_maker'),
    # path('rock_paper_game/', views.game_function, name='game')
]

