from django import forms
from .models import TodoItem
from datetime import date




class TodoForm(forms.ModelForm):

  class Meta:
    model = TodoItem
    fields = ('item_number', 'task', 'created_date', 'date_due', 'time_due')

    


