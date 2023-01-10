from django import forms

css_classes = ""

class BaseForm(forms.Form):
    username = forms.CharField(max_length=32, min_length=3, widget=forms.TextInput)
    password = forms.CharField(
        widget=forms.PasswordInput(), min_length=8, max_length=64)

class RegisterForm(BaseForm):
    email = forms.EmailField()
    password_confirmation= forms.CharField(
        widget=forms.PasswordInput(), min_length=8, max_length=64)