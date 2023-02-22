from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    cohort = models.CharField(max_length=100)
    favorite_language = models.CharField(max_length=100)
    capstone = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
