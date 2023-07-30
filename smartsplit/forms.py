from django import forms
#from django.forms import Form

class sendMoneyForm(forms.Form):
    amount = forms.FloatField(required=True, widget=forms.TextInput(attrs={'placeholder': 'USD amount'}))
    recipient = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'recipient username'}))
                                      