from django.db import models


class TodoItem(models.Model):
  text = models.CharField(max_length=100)
  created_date =  models.DateTimeField(null=True, blank=True)

  def __str__(self):
        return self.text
