from django import forms

class user_input(forms.Form):
    
    input = forms.CharField(
        label="", 
        max_length=1024, 
        widget=forms.TextInput(
            attrs={'placeholder':'enter to do task'}
        )
    )