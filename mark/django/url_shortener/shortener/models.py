from django.db import models


# Create your models here.
class ShortenedURL(models.Model):
    code = models.CharField(max_length=6)
    url = models.URLField()
    counter = models.IntegerField(default = 0)
    
    def __str__(self):      
        return self.code + '--' + self.url
    
#  Shortend URL Table
#  | id | code | url |
#  -------------------

