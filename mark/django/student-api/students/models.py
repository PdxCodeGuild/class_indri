from django.db import models

# Create your models here.
class Students(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    cohort = models.CharField(max_length=50)
    fav_language = models.CharField(max_length=25)
    capstone = models.URLField(max_length=200)
    
    def __str__(self):
        return f"{self.last_name}, {self.first_name} - {self.cohort} : {self.capstone}"