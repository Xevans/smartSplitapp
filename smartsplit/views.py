from django.shortcuts import render
from django.views.generic import TemplateView
from accounts.models import *

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
