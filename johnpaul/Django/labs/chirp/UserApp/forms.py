from django.contrib.auth.models import User
from django import forms
import datetime

class BaseForm(forms.Form):
  username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'style': 'width: 300px;'}))
  password = forms.CharField(widget=forms.PasswordInput(attrs={'style': 'width: 300px;'}), min_length=8, max_length=32)


class SignUpForm(BaseForm):
  password_confirmation = forms.CharField(widget=forms.PasswordInput(attrs={'style': 'width: 300px;'}), min_length=8, max_length=32)
  first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'style': 'width: 300px;'}))
  last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'style': 'width: 300px;'}))
  email = forms.EmailField(widget=forms.TextInput(attrs={'style': 'width: 300px;'}))


  