from django.urls import path
from . import views

# URL Conf
urlpatterns = [
    path("", views.index, name="welcomepage"),
    path('to_do_list/', views.make_list, name='list')
   
]