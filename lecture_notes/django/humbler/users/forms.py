from django import forms


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=32, min_length=3)
    email = forms.EmailField()
    password = forms.CharField(
        widget=forms.PasswordInput(), min_length=8, max_length=32)
    password_confirmation = forms.CharField(
        widget=forms.PasswordInput(), min_length=8, max_length=32)
