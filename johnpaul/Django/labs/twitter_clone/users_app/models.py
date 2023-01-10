from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
  username = models.CharField(max_length=50, unique=True)
  user_email = models.EmailField(max_length=50, unique=True, blank=False)
  first_name =models.CharField(max_length=50)
  last_name =models.CharField(max_length=50)
  password = models.CharField(max_length=50)
  password_confirmation = models.CharField(max_length=50)

  def __str__(self):
    return self.user.username
