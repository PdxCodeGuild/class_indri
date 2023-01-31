from django.urls import path
from .views import ListStudents, ChangeStudents

urlpatterns = [
    path("", ListStudents.as_view()),
    # path("completed/", ListCompletedTodos.as_view()),
     path("<int:pk>/", ChangeStudents.as_view())
]