from django import forms

class InsultForm(forms.Form):
    password = forms.CharField(max_length=100, label='Enter Password')