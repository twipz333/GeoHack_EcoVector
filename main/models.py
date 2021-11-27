from django.db import models
from django.db.models.expressions import Value

# Create your models here.
class User(models.Model):
    uid = models.CharField(max_length=20, unique=True, null=False, editable=False)
    tg_uid = models.CharField(max_length=9, unique=True, editable=False, null=True)
    vk_uid = models.CharField(max_length=20, unique=True, editable=False,null=True)
    username = models.CharField(max_length=15, unique=True, null=True)
    password = models.CharField(max_length=200, null=True)

    def subscribe(self, event):
        if isinstance(event, Event):
            sub = Subscription(user=self, event=event)
            sub.save()

    def unsubscribe(self, event):
        if isinstance(event, Event):
            sub = Subscription.objects.get(user=self,event=event)
            if sub:
                sub.delete()
            #else:
            #    raise Not

    def __str__(self):
        return self.uid

class Event(models.Model):
    name = models.CharField(max_length=20, unique_for_date="date")
    description = models.TextField(max_length=250)
    date = models.DateTimeField("date of event",auto_now=False, auto_now_add=False)
    # attachment = models.FilePathField()

    def subscribe(self, user):
        if isinstance(user, User):
            sub = Subscription(user=user, event=self)
            sub.save()

    def unsubscribe(self, user):
        if isinstance(user, User):
            sub = Subscription.objects.get(user=user, event=self)
            if sub:
                sub.delete()
            #else:

    def __str__(self) -> str:
        return self.name

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.user} -> {self.event}'

    