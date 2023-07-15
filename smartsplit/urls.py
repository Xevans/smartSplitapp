from django.urls import path
from .views import Welcome, Homepage, Account

urlpatterns = [
    path("", Welcome.as_view(), name="welcome"), # when a user visits websitName.com/ they will be directed to the view, welcome
    path("home/", Homepage.as_view(), name="home"),
    path("account/", Account.as_view(), name="account")
]