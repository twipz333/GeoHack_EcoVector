from django.db import models
from django.db.models.expressions import F, Value
import json

# Create your models here.
class User(models.Model):
    #uid = models.CharField(max_length=20, unique=True, null=True, blank=False, editable=False)
    tg_uid = models.CharField(max_length=9, unique=True, null=True, blank=True, editable=False)
    vk_uid = models.CharField(max_length=20, unique=True, null=True, blank=True, editable=False)
    username = models.CharField(max_length=15, unique=True, null=True, blank=True, editable=True)
    password = models.CharField(max_length=200, unique=False, null=True, blank=True, editable=True)
    email = models.EmailField(max_length=30, unique=True, blank=True, null=True, editable=True)
    phone = models.CharField(max_length=11, unique=True, null=True, blank=True, editable=True)
    tag = models.TextField(max_length=1024, unique=False, null=True, blank=False, editable=True, default=r'{}')

    def update(self, data: dict):
        #self.uid = data.get('uid') if data.get('uid') else self.uid
        self.tg_uid = data.get('tg_uid') if data.get('tg_uid') else self.tg_uid
        self.vk_uid = data.get('vk_uid') if data.get('vk_uid') else self.vk_uid
        self.username = data.get('username') if data.get('username') else self.username
        self.password = data.get('password') if data.get('password') else self.password
        self.email = data.get('email') if data.get('email') else self.email
        self.phone = data.get('phone') if data.get('phone') else self.phone
        self.tag = data.get('tag') if data.get('tag') else self.tag

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

    def get_subscriptions(self):
        return Subscription.objects.filter(user=self)

    def add_tags(self, tags):
        _tags = json.loads(self.tag)
        for k, v in tags:
            _tags[k] = v
        self.tag = json.dumps(_tags)

    def remove_tags(self, tags):
        _tags = json.loads(self.tag)
        for k in tags:
            if k in _tags.keys():
                del _tags[k]
        self.tag = json.dumps(_tags)

    def get_tags(self):
        return json.load(self.tag)

    def __str__(self):
        return self.id

class Event(models.Model):
    name = models.CharField(max_length=20, unique_for_date="date")
    description = models.TextField(max_length=250, null=True)
    date = models.DateTimeField("date of event",auto_now=False, auto_now_add=False)
    verified = models.BooleanField(default=False)
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
    comment = models.TextField(max_length=1024, unique=False, null=True, blank=True, editable=True)
    rating = models.PositiveSmallIntegerField(unique=False, null=True, blank=True, editable=True)

    def __str__(self) -> str:
        return f'{self.user} -> {self.event}'

    