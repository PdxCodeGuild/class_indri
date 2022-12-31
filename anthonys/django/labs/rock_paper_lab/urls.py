from django.urls import path
from . import views

# URL Conf
urlpatterns = [
    path("", views.index, name="homepage"),
    path('password_generator/', views.password_generator, name='password_maker'),
    # path("rps/", views.rps, name="rps"),
    # path("rps/<str:user_choice>/", views.rps_game, name="rps_game")
    path('rock_paper_game/', views.rocks_paper_score, name='rps_score'),
    path("rock_paper_game/<str:user_pick>/", views.game_function, name="game")
]


