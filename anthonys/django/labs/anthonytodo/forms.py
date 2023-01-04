from django import forms

# Create a new form class called URLForm
class ToDoForm(forms.Form):
    # The field is rendered as a text input with a placeholder attribute
    to_do = forms.CharField(label="", max_length=2048, widget=forms.TextInput(
        attrs={'placeholder': 'Input a task'}))