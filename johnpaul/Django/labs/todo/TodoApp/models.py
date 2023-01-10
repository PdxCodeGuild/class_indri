from django.db import models
from django.urls import reverse
import datetime




class TodoItem(models.Model):
  task = models.CharField(max_length=100)
  created_date =  models.DateTimeField(null=True, blank=True)
  time_due = models.TimeField(default=datetime.time(hour=0, minute=0))
  date_due = models.DateTimeField(null=True, blank=True)
  item_number = models.IntegerField(default=0)


  def __str__(self):
        return self.task

  def get_absolute_url(self):
      return reverse("home", kwargs={"pk": self.pk})
  

