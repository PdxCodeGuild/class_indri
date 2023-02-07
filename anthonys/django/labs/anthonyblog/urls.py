from django.urls import path
from . import views

# URL Conf
# urlpatterns = [
#     path("", views.blogs, name="bloghome")
#     # path('admin/',)
# ]

urlpatterns = [
    path("", views.index, name="bloghome"),
    path("create/", views.create, name="create"),
    path("edit/<int:blog_id>/", views.edit, name="edit")
]