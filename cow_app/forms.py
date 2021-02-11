from django import forms
from cow_app.models import CowText

class CowTextForm(forms.Form):
    speak = forms.CharField(max_length=150)