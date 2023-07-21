from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class Welcome(TemplateView):
    template_name = "welcome.html"

class Homepage(TemplateView):
    template_name = "home.html"

class Account(TemplateView):
    template_name = "account.html"

class editProfile(TemplateView):
    template_name = "edit_profile.html"