from django import forms


class URLForm(forms.Form):
    url = forms.URLField(label="", max_length=2048, widget=forms.TextInput(
        attrs={'placeholder': 'Enter url to be shortened'}))