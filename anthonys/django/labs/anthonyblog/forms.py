from django import forms
from .models import BlogData


# Use the ModelForm class to create a form based on the BlogPost model
class NewBlogForm(forms.ModelForm):
    class Meta:
        # Specify the model to use
        model = BlogData
        # Define the fields that should be included in the form
        fields = ("title", "body", "public")