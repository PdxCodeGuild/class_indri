
from django.urls import path

from . import views

# localhost:8000/users/
urlpatterns = [
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile")
]
