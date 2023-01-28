from django.urls import path
from .views import StudentList, StudentActions, StudentSearch
from . import views

urlpatterns = [
    path('index/', views.index),
    path('', StudentList.as_view()),
    path('<int:pk>', StudentActions.as_view()),
    path('students/<str:first_name>', StudentSearch.as_view())
]
