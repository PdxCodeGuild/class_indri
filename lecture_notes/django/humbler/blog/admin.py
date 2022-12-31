from django.contrib import admin
from .models import BlogPost

# Adds BlogPost model to admin site
admin.site.register(BlogPost)
