from django.urls import path
from .views import Welcome, Homepage, account, sendMoney, send_success

urlpatterns = [
    path("", Welcome.as_view(), name="welcome"), # when a user visits websitName.com/ they will be directed to the view, welcome
    path("home/", Homepage.as_view(), name="home"),
    path("account/", account, name="user-account"),
    path("send_cash/", sendMoney, name="send_cash"),
    path("send_success/", send_success, name="send_success")
]