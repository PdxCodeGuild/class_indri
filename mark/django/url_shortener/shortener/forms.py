from django import forms

class URLForm(forms.Form):
    url = forms.URLField(max_length=2048, label="Enter URL to be shortened")