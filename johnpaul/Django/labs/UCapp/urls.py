from django.urls import path
from . import views

app_name = 'UCapp'

urlpatterns = [
    path('', views.home, name='home'),
]