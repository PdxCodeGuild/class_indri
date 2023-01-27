from django import forms
from .models import Post

class NewPost(forms.ModelForm):
    class Meta:
        
        model = Post
        
        fields = ("body", "public", "image")