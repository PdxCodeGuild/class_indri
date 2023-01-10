from django import forms
from .models import Hoot


class HootForm(forms.ModelForm):
    class Meta:
        model = Hoot
        fields = ('title', 'hoot', 'public')