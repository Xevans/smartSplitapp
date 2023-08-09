from django.contrib import admin
from .models import Requests, SentHistory, FriendRequests, FriendList

# Register your models here.
admin.site.register(Requests)
admin.site.register(SentHistory)
admin.site.register(FriendRequests)
admin.site.register(FriendList)
