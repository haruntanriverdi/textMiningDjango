from django import forms
from .models import Main

class MainForm(forms.Form):

    upload1 = forms.ImageField(required=True, widget = forms.FileInput(attrs={'class':'form-control'}))

    upload2 = forms.ImageField(required=True, widget = forms.FileInput(attrs={'class':'form-control'}))



