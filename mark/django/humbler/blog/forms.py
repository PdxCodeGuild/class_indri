from django import forms
from users.models import BlogPost

class NewPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ("title", "body", "public", "image")