from django.urls import path
from .views import StudentList, StudentDetail
from .views import StudentFilter

urlpatterns = [
    path('', StudentList.as_view()),
    path('<int:pk>/', StudentDetail.as_view()),
    path('<str:capstone>/', StudentFilter.as_view()),
]