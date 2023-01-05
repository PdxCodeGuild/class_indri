from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_home, name = 'home'),
    path('post_create/', views.post_create, name = 'create-post'),
    path('post_detail/', views.post_detail, name = 'post-detail'),
]
