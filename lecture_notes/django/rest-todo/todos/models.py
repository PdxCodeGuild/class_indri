from django.db import models

"""
Todo
title - Walk the dog
description - Walk the dog for at least 2 miles
completed - False
"""


class Todo(models.Model):
    title = models.CharField(max_length=75)
    description = models.CharField(max_length=250)
    completed = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        # (False) Walk the dog - Walk the dog for at least 2 miles
        return f"({self.completed}) {self.title} - {self.description}"
