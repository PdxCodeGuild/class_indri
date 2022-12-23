from django import forms

class TodoForm(forms.Form):
    todo = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'What needs to be done?'}))

    