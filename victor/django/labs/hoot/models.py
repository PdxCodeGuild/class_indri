from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Hoot(models.Model):
    title = models.CharField(max_length=100)
    hoot = models.CharField(max_length=240)
    public = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title + ' ' + self.user.username
