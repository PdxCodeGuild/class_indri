from django import forms


class BaseForm(forms.Form):
    username = forms.CharField(max_length=32, min_length=4)
    password = forms.CharField(
        widget=forms.PasswordInput(), min_length=8, max_length=32
    )


class CreateProfileForm(BaseForm):
    email = forms.EmailField()
    password_confirmation = forms.CharField(min_length=8, max_length=32)