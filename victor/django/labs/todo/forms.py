from django import forms

class TodoForm(forms.Form):
    todo = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'What needs to be done?'}))

    