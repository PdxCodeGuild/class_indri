from django import forms


class BaseForm(forms.Form):
    username = forms.CharField(required=True, max_length=32, min_length=3)
    password = forms.CharField(required=True, widget=forms.PasswordInput(), min_length=8, max_length=32)

    
class RegistrationForm(BaseForm):
    email = forms.EmailField()
    password_confirmation = forms.CharField(required=True, widget=forms.PasswordInput(), min_length=8, max_length=32)

