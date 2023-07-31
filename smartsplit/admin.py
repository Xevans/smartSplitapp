from django.contrib import admin
from .models import Requests, SentHistory

# Register your models here.
admin.site.register(Requests)
admin.site.register(SentHistory)