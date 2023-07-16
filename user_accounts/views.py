from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.

class SignUpView(generic.CreateView): # Note to self, generic.CreateView is a generic-based-view
    form_class = UserCreationForm
    success_url = reverse_lazy("login") # redirect to login when sign up is completed
    template_name = "registration/signup.html"
