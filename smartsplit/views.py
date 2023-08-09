from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from .forms import sendMoneyForm, requestMoneyForm, sendFriendRequestForm, acceptFriendRequestForm
from .models import Requests, SentHistory, FriendRequests, FriendList
from django.contrib.auth.models import User
import decimal
from django.db.models import Q # for making complex queries to the db

# Create your views here.
class Welcome(TemplateView):
    template_name = "welcome.html"

### home view ###
def homepage(request):

    #POST
    if request.method == "POST":
        #print(request.POST['accept']) # prints name of sender
        
        # handle accept/reject friend request buttons
        # POST contains a list of POST information. We want to see if either accept or reject as identified in the template have been sent
        # if so, do something.
        if 'accept' in request.POST:

            friend_request = FriendRequests.objects.get(sender=request.POST['accept']) # look up the friend request object that has a matching username.The name of the button is tied to its value. in this case, it is the name of the user who sent it
            friend_request.status = "accept"
            friend_request.save()

            this_friend_username = request.POST['accept']

            new_friend = FriendList.objects.create(this_user=request.user, friend_username=this_friend_username)
            new_friend.save()


        if 'reject' in request.POST:
            friend_request = FriendRequests.objects.get(sender=request.POST['reject'])
            friend_request.status = "reject"
            friend_request.save()

            friend_request.delete()

        return HttpResponseRedirect('/home')
    
    #GET
    else:
        this_user = request.user.username # get current user's username
        requests_from_this_user = Requests.objects.filter(Q(sender=this_user)) # obtain a queryset containing every request object that meets the lookup criteria
        requests_to_this_user = Requests.objects.filter(Q(recipient=this_user))

        payment_from_this_user = SentHistory.objects.filter(Q(sender=this_user))
        payment_to_this_user = SentHistory.objects.filter(Q(recipient=this_user))

        accepted_friend_requests = FriendRequests.objects.filter(Q(status="accept"))
        incoming_friend_requests = FriendRequests.objects.filter(Q(recipient=this_user, status="pending")) # only show requests that are pending

        for item in accepted_friend_requests:
            new_friend = FriendList.objects.create(this_user=request.user, friend_username=item.recipient)
            new_friend.save()
            item.delete()


        #print(payment_from_this_user.values_list())
        #print(this_user)
        #print(requests_from_this_user.values_list())
        #a = requests_from_this_user.values_list()
        
        #for records in requests_from_this_user:
            #print(records.recipient)
        return render(request, "home.html", {'outgoing_requests':requests_from_this_user, 'incoming_requests':requests_to_this_user, 'outgoing_payments':payment_from_this_user, 'incoming_payments':payment_to_this_user, 'friend_requests':incoming_friend_requests}) # name of queryset for template to reference : actual queryset in this function



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

            this_user = request.user.username # username of current user
            this_amount = form.cleaned_data['amount'] # amount to send
            send_to = str(form.cleaned_data['recipient']) # username of recipient to send to
            this_message = str(form.cleaned_data['message']) # message to send the recipient

            
            # attempt to prevent leading zeroes and misconversions
            x = decimal.Decimal(this_amount)
            y = decimal.Decimal(request.user.profile.balance)

            if request.user.profile.balance < this_amount or this_amount < 0:
                form = sendMoneyForm()
                return render(request, "send_cash.html", {"form": form})
                #raise ValidationError('Number must be positive')
                

            else:
                z = y - x
                request.user.profile.balance = z
                request.user.save()

                recipient = User.objects.get(**{User.USERNAME_FIELD: send_to})
                
                x = decimal.Decimal(this_amount)
                y = decimal.Decimal(recipient.profile.balance)
                z = y + x

                recipient.profile.balance = z
                recipient.save()

                # create and save new request object
                new_payment = SentHistory.objects.create(sender=this_user, message=this_message, request_amount=this_amount, recipient=send_to)
                new_payment.save()
            
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



def send_friend_request(request):
    
    friends = FriendList.objects.filter(Q(this_user=request.user))
    print(friends)
    
    if request.method == "POST":
        form = sendFriendRequestForm(request.POST) # create form obj with details from form on page
        
        if form.is_valid():
            #extract form data
            #create friend request object and save it
            this_user = request.user.username
            send_to = form.cleaned_data['recipient']
            this_message = form.cleaned_data['message']

            friend_request = FriendRequests.objects.create(sender=this_user, message=this_message, recipient=send_to, send_status=True)
            friend_request.save()

            return HttpResponseRedirect('/friend_request_success')
    else:
        form = sendFriendRequestForm()

    return render(request, "send_friend_request.html", context={'form':form, 'friends':friends})



def send_friend_request_success(request):
    return render(request, "send_friend_request_success.html")