from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator #add a message in views.py to show error message to user


class InputForm(forms.Form):
  password_length = forms.IntegerField(label='Enter length of password: ', widget=forms.TextInput(attrs={'placeholder':'minimum length 8'}), validators=[MinValueValidator(8)])