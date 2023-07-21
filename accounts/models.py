from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    pass
    # additional fields here
    #test_identifier = models.CharField(max_length=40, unique=False)
    #groups
    #total balances owed
    #phone number

    def __str__(self):
        return self.username
