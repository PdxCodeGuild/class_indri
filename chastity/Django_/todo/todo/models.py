from django.db import models

#  Create your models here.
class TodoItem(models.Model):
    title = models.CharField(max_length=200, null=True)
    complete = models.DateTimeField(null=True)
    created = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.title