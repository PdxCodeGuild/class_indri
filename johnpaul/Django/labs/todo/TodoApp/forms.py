from django import forms
from .models import TodoItem


class TodoForm(forms.Form):
  text = forms.CharField(max_length=250)