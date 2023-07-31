from django import forms
#from django.forms import Form

class sendMoneyForm(forms.Form):
    message = forms.CharField(max_length = 200, required = True, widget=forms.TextInput(attrs={'placeholder': 'Whats it for?'}))
    amount = forms.FloatField(required=True, widget=forms.TextInput(attrs={'placeholder': 'USD amount'}))
    recipient = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Recipient username'}))


class requestMoneyForm(forms.Form):
    message = forms.CharField(max_length = 200, required = True, widget=forms.TextInput(attrs={'placeholder': 'Whats it for?'}))
    amount = forms.FloatField(required=True, widget=forms.TextInput(attrs={'placeholder': 'USD amount'}))
    requestee = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Requestee username'}))


