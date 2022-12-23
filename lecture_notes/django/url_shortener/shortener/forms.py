from django import forms

# Create a new form class called URLForm
class URLForm(forms.Form):
    # Define a 'url' field as a URLField with a maximum length of 2048 characters
    # The field is rendered as a text input with a placeholder attribute
    url = forms.URLField(label="", max_length=2048, widget=forms.TextInput(
        attrs={'placeholder': 'Enter url to be shortened'}))