from django import forms


# Create a form class that inherits from forms.Form
class BaseForm(forms.Form):
    username = forms.CharField(max_length=32, min_length=3)
    password = forms.CharField(
        widget=forms.PasswordInput(), min_length=8, max_length=32)


# Create a form class that inherits from BaseForm
class RegistrationForm(BaseForm):
    email = forms.EmailField()
    password_confirmation = forms.CharField(min_length=8, max_length=32)
