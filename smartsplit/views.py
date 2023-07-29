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
    context = {'test':Profile.objects.all()}
    return render(request, "account.html", context)
