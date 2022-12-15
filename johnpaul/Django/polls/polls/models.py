from django.db import models

# Create your models here.
# Models are python representation of a sql table
# Each class is a new table
# properties on the class are columns


class Question(models.Model):
  question_text = models.CharField(max_length = 100)
  pub_date = models.DateTimeField

  def __str__(self):
    return self.question_text

class Choice(models.Model):
  choice_text = models.CharField(max_length = 100)
  votes = models.IntegerField(default=0)
  question = models.ForeignKey(Question, on_delete=models.CASCADE)

  def __str__(self):
    return f"({self.votes}) -- {self.choice_text}"



