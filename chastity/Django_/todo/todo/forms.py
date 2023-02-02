from django import forms

class TodoItemForm(forms.Form):
    input = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(
            attrs={'Placeholder': 'To Do Item'}
        )
    )