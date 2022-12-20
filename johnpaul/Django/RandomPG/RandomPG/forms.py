from django import forms


class InputForm(forms.Form):
  password_length = forms.IntegerField(label='Enter length of password: ', widget=forms.TextInput(attrs={'placeholder':'minimum length 8'}))