from django import forms


css_classes = ""


class BaseForm(forms.Form):
    username = forms.CharField(
        max_length=32, min_length=3, widget=forms.TextInput(attrs={"class": css_classes}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": css_classes}), min_length=8, max_length=32)


class RegistrationForm(BaseForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": css_classes}))
    password_confirmation = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": css_classes}), min_length=8, max_length=32)
