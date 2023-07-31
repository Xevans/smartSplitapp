from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import Profile
from smartsplit.models import Requests


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()



#We dont need to create a payment request object for every user that is created.
# we will create a request object when a payment request is created.
#@receiver(post_save, sender=Profile)
#def create_requests(sender, instance, created, **kwargs):
#    if created:
#        Requests.objects.create(user=instance)

#@receiver(post_save, sender=Profile)
#def save_requests(sender, instance, **kwargs):
#    instance.requests.save()