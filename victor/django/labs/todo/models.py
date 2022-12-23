from django.db import models


# Create your models here.
class Todo(models.Model):
    text = models.CharField(max_length=100, null=True, blank=True)
    created_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.text
    
 