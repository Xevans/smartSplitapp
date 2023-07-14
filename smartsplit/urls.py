from django.urls import path
from .views import Welcome

urlpatterns = [
    path("", Welcome.as_view(), name="home") # when a user visits websitName.com/ they will be directed to the view, welcome
]