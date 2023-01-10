from django.db import models

# Create your models here.
class TodoItem(models.Model):
    # Define a 'text' field as a CharField 
    text=models.CharField(max_length=75)
    # Define a create_date field as a create date
    created_date=models.DateTimeField(blank=True, null=True)
    # Define the return the text
    def __str__(self):
        return self.text + " -- " + self.created_date
