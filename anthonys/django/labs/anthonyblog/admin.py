
from django.contrib import admin
from .models import BlogData

# Register your models here.
# Adds BlogPost model to admin site
admin.site.register(BlogData)