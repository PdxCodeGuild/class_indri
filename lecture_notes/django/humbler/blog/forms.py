from django import forms
from .models import BlogPost


# Use the ModelForm class to create a form based on the BlogPost model
class NewPostForm(forms.ModelForm):
    class Meta:
        # Specify the model to use
        model = BlogPost
        # Define the fields that should be included in the form
        fields = ("title", "body", "public", "image")
