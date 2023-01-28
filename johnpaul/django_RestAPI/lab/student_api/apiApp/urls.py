from django.urls import path
from .views import StudentCreate, StudentDetail
from .views import StudentList

urlpatterns = [
    path('', StudentCreate.as_view()),
    path('<int:pk>/', StudentDetail.as_view()),
    path('students/<str:first_name>/', StudentList.as_view(), name='student-list'),
]