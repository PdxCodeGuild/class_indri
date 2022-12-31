from django.contrib.auth.models import User
from django import forms
import datetime

class BaseForm(forms.Form):
  username = forms.CharField(max_length=50)
  password = forms.CharField(widget=forms.PasswordInput(), min_length=8, max_length=32)


class SignUpForm(BaseForm):
  password_confirmation = forms.CharField(widget=forms.PasswordInput(), min_length=8, max_length=32)
  first_name = forms.CharField(max_length=50)
  last_name = forms.CharField(max_length=50)
  email = forms.EmailField()
  email = forms.EmailField()
  date_of_birth = forms.DateField()