from django.urls import path
from .views import AllStudents, DetailStudents

urlpatterns = [
    path("", AllStudents.as_view()),
    path("<int:pk>/", DetailStudents.as_view()),
    # path("student/", SelectStudent.as_view())
]