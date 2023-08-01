from django.urls import path
from .views import Welcome, homepage, account, sendMoney, send_success, requestMoney, request_success

urlpatterns = [
    path("", Welcome.as_view(), name="welcome"), # when a user visits websitName.com/ they will be directed to the view, welcome
    path("home/", homepage, name="home"),
    path("account/", account, name="user-account"),
    path("send_cash/", sendMoney, name="send_cash"),
    path("send_success/", send_success, name="send_success"),
    path("request_money/", requestMoney, name="request_money"),
    path("request_success/", request_success, name="request_success")
]