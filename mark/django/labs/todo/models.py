from django.db import models

class TodoItem(models.Model):
    entry = models.CharField(max_length=1024)
    created = models.DateTimeField(auto_now=True)
    completed = models.DateTimeField(null=True)

# id | entry | created