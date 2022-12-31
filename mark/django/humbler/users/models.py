from django.db import models
from django.contrib.auth.models import User

"""
BlogPost
    title (CharField)
    body (TextField)
    user (ForeignKey to django.contrib.auth.models.User)
    public (BooleanField)
    date_created (DateTimeField with auto_now_add=True)
    date_edited (DateTimeField with auto_now=True)
"""

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    public = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="blog_images/", blank=True)
    
    
    def __str__(self):
        return self.title + " - " + self.user.username