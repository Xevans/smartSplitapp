from django.urls import path
from .views import Welcome, Homepage, account

urlpatterns = [
    path("", Welcome.as_view(), name="welcome"), # when a user visits websitName.com/ they will be directed to the view, welcome
    path("home/", Homepage.as_view(), name="home"),
    path("account/", account, name="user-account"),
]