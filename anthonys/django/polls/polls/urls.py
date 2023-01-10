from django.urls import path
from . import views
urlpatterns = [
path("", views.index, name='index'),
#localhost:8000/detial/1
path("detail/<int:question_id>", views.detail, name="detail"),
#localhost:8000/results/1
path("results/<int:question_id>", views.results, name="results"),
#localhost:8000/vote/1
path("vote/<int:question_id>", views.vote, name="vote")
]
