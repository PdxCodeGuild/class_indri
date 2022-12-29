from django.urls import path
from .import views

urlpatterns = [
    path('user_post/', views.post, name='user_post'),
]