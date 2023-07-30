from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from .forms import sendMoneyForm
from accounts.models import Profile
from django.contrib.auth.models import User
#from accounts.models import *

# Create your views here.
class Welcome(TemplateView):
    template_name = "welcome.html"

class Homepage(TemplateView):
    template_name = "home.html"

#class Account(TemplateView):
#    template_name = "account.html"


def account(request):
    #request.user.profile.balance -= 1.00
    #request.user.save()
    return render(request, "account.html")


def sendMoney(request):
    if request.method == "POST":
        # creat a form instance and populate it based on what the user filled in the forms
        form = sendMoneyForm(request.POST)
        
        if form.is_valid():
            # process data here
            # subtract from this user's balance
            # add to recipient user's balance
            #commit changes

            amount = form.cleaned_data['amount']
            send_to = str(form.cleaned_data['recipient'])

            request.user.profile.balance -= amount
            request.user.save()

            recipient = User.objects.get(**{User.USERNAME_FIELD: send_to})
            recipient.profile.balance += amount
            recipient.save()
            #print(recipient.profile.balance)
            return HttpResponseRedirect('/send_success') # take to a success page confirming their payment was sent
        
    else: # if GET request or any other method, create a blank form (render the page with the sendMoneyForm)
        form = sendMoneyForm()

    return render(request, "send_cash.html", {"form": form})

def send_success(request):
    return render(request, "send_success.html")