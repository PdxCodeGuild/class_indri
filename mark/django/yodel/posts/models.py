from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Post(models.Model):
    body = models.TextField(max_length=280)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    public = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)