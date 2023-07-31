from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from .forms import sendMoneyForm, requestMoneyForm
from accounts.models import Profile
from .models import Requests
from django.contrib.auth.models import User
import decimal
from django.db.models import Q # for making complex queries to the db


# Create your views here.


### welcome view ###
class Welcome(TemplateView):
    template_name = "welcome.html"


### home view ###
def homepage(request):
    this_user = request.user.username # get this user's username
    requests_from_this_user = Requests.objects.filter(Q(sender=this_user)) # obtain a queryset containing every request object that meets the lookup criteria
    requests_to_this_user = Requests.objects.filter(Q(recipient=this_user))
    #print(this_user)
    #print(requests_from_this_user.values_list())
    #a = requests_from_this_user.values_list()
    
    #for records in requests_from_this_user:
        #print(records.recipient)
    return render(request, "home.html", {'outgoing_requests':requests_from_this_user, 'incoming_requests':requests_to_this_user}) # name of queryset for template to reference : actual queryset in this function




### account view ###
def account(request):
    #request.user.profile.balance -= 1.00
    #request.user.save()
    return render(request, "account.html")




### send_money view ###
def sendMoney(request):
    if request.method == "POST":
        # creat a form instance and populate it based on what the user filled in the forms
        form = sendMoneyForm(request.POST)
        
        if form.is_valid():
            # process data here
            # subtract from this user's balance
            # add to recipient user's balance
            #commit changes

            amount = form.cleaned_data['amount'] # amount to send
            send_to = str(form.cleaned_data['recipient']) # username of recipient to send to
            message = str(form.cleaned_data['message']) # message to send the recipient

            
            # attempt to prevent leading zeroes and misconversions
            x = decimal.Decimal(amount)
            y = decimal.Decimal(request.user.profile.balance)
            z = y - x

            request.user.profile.balance = z
            request.user.save()

            recipient = User.objects.get(**{User.USERNAME_FIELD: send_to})
            
            x = decimal.Decimal(amount)
            y = decimal.Decimal(recipient.profile.balance)
            z = y + x

            recipient.profile.balance = z
            recipient.save()
            #print(recipient.profile.balance)
            return HttpResponseRedirect('/send_success') # take to a success page confirming their payment was sent
        
    else: # if GET request or any other method, create a blank form (render the page with the sendMoneyForm)
        form = sendMoneyForm()

    return render(request, "send_cash.html", {"form": form})



### request_money view ###
def requestMoney(request):
    if request.method == "POST":
        
        form = requestMoneyForm(request.POST)

        if form.is_valid():
            this_user = request.user.username # username of sender (current user object is always stored in request)
            this_amount = form.cleaned_data['amount'] # amount to send
            requestee_name = str(form.cleaned_data['requestee']) # username of person to send to.
            this_message = str(form.cleaned_data['message']) # message for recipient of request

            #requestee = User.objects.get(**{User.USERNAME_FIELD: requestee_name}) # look up the recipient in the User table by username

            # create and save new request object
            new_request = Requests.objects.create(sender=this_user, message=this_message, request_amount=this_amount, recipient=requestee_name)
            new_request.save()

        return HttpResponseRedirect('/request_success')
    
    else:
        form = requestMoneyForm()

    return render(request, "request_money.html", {"form": form})



### send_success view ###
def send_success(request):
    return render(request, "send_success.html")


### request_success view ###
def request_success(request):
    return render(request, "request_success.html")