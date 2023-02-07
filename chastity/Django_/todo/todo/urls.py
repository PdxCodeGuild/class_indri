from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("save", views.save_tasks, name="save_tasks"),
    path('remove/<int:id>', views.remove_tasks, name="remove_tasks"),
    path('finished/<int:id>', views.finished_tasks, name='finished_tasks'),
               
]