from django.db import models
from django.contrib.auth.models import User


# payment request model
class Requests(models.Model):
    sender = models.CharField(max_length=100, default="")
    message = models.CharField(max_length=200, default = "")
    request_amount = models.FloatField(max_length=100, default = 0.00)
    recipient = models.CharField(max_length=100, default="")


# Transaction History Model
class SentHistory(models.Model):
    sender = models.CharField(max_length=100, default="")
    message = models.CharField(max_length=100, default="")
    request_amount = models.FloatField(max_length=100, default = 0.00)
    recipient = models.CharField(max_length=100, default="")

    
# Friend request model
class FriendRequests(models.Model):
    sender = models.CharField(max_length=100, default="")
    message = models.CharField(max_length=100, default="")
    recipient = models.CharField(max_length=100, default="")
    status = models.CharField(max_length=30, default="pending")
    send_status = models.BooleanField(default=False)

    

# Friend list Model
class FriendList(models.Model):
    this_user = models.ForeignKey(User, on_delete=models.CASCADE)
    friend_username = models.CharField(max_length=100, default="")
