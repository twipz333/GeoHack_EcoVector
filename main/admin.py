from django.contrib import admin
from .models import User, Event, Subscription

admin.site.register(Event)
admin.site.register(User)
admin.site.register(Subscription)
# Register your models here.
