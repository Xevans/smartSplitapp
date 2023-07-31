from django.db import models
from accounts.models import User

# payment request model
class Requests(models.Model):
    sender = models.CharField(max_length=100, default="")
    message = models.CharField(max_length=200, default = "")
    request_amount = models.FloatField(max_length=100, default = 0.00)
    recipient = models.CharField(max_length=100, default="")