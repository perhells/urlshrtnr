from django import forms

class CreateForm(forms.Form):
    url = forms.CharField(max_length=1000)
    shortened = forms.CharField(max_length=200)
