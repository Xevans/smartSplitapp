from django.urls import path
from .views import welcome

urlpatterns = [
    path("", welcome, name="home") # when a user visits websitName.com/ they will be directed to the view, welcome
]