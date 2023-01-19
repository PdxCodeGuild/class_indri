from django.db import models
from django.contrib.auth.models import User

class BlogData(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    public = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)
    

    # Define the string representation of a BlogPost
    def __str__(self):
        # title - username
        return self.title + " - " + self.user.username
