from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    cohort = models.CharField(max_length=32)
    favorite_language = models.CharField(max_length=32)
    capstone = models.URLField(max_length=100)
    
    def __str__(self):
        return self.first_name + " " + self.last_name
