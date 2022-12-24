from django.db import models

class ShortenedURL(models.Model):
    code = models.CharField(max_length=6)
    url = models.URLField()
    counter = models.IntegerField(default=0)

    def __str__(self):
        return self.code + " -- " + self.url


""" ShortendURL Table
| id | code | url | 
-------------------

"""