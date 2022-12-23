from django.db import models

# Create a new model class called ShortenedURL
class ShortenedURL(models.Model):
    # Define a 'code' field as a CharField with a maximum length of 6 characters
    code = models.CharField(max_length=6)
    # Define a 'url' field as a URLField
    url = models.URLField()
    # Define a 'counter' field as an IntegerField with a default value of 0
    counter = models.IntegerField(default=0)

    # Define the "__str__" method to return the code and URL when a ShortenedURL object is printed
    def __str__(self):
        return self.code + " -- " + self.url



"""Explanation:
Django model is a class that represents a database table. In this case, the ShortenedURL model represents a table in the database that stores information about shortened URLs.

The model has three fields:

code: a CharField with a maximum length of 6 characters. This field will store the unique code that is used to access the shortened URL.

url: a URLField. This field will store the original URL that the shortened URL corresponds to.

counter: an IntegerField with a default value of 0. This field will store a counter that keeps track of how many times the shortened URL has been accessed.

The __str__ method is a special method in Python that is called when an object is printed. In this case, the __str__ method returns a string representation of the ShortenedURL object, which consists of the code and URL separated by a double dash (" -- "). This string representation will be used when a ShortenedURL object is printed.
"""


""" ShortendURL Table
| id | code | url | 
-------------------

"""