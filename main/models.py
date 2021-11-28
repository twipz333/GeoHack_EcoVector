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
    tags = models.TextField(max_length=1024, unique=False, null=True, blank=False, editable=True, default=r'{}')
    pref_channel = models.CharField(max_length=4,choices=[('tg','telegramm'),('vk','vkontakte'),('site','site'),('na','not set')], default='na',blank=True)
    is_staff = models.BooleanField(default=False, blank=True)

    def update(self, data: dict):
        #self.uid = data.get('uid') if data.get('uid') else self.uid
        self.tg_uid = data.get('tg_uid') if data.get('tg_uid') else self.tg_uid
        self.vk_uid = data.get('vk_uid') if data.get('vk_uid') else self.vk_uid
        self.username = data.get('username') if data.get('username') else self.username
        self.password = data.get('password') if data.get('password') else self.password
        self.email = data.get('email') if data.get('email') else self.email
        self.phone = data.get('phone') if data.get('phone') else self.phone
        self.tag = data.get('tag') if data.get('tag') else self.tag
        self.pref_channel = data.get('pref_channel') if data.get('pref_channel') else self.pref_channel
        self.is_staff = data.get('is_staff') if data.get('is_staff') else self.is_staff
        self.save()

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
    date = models.CharField(max_length=20, unique=False, blank=True, null=True, editable=True)
    verified = models.BooleanField(default=False)
    place = models.CharField(max_length=100, unique=False, blank=True, null=True, editable=True)
    tags = models.TextField(max_length=1024, unique=False, null=True, blank=False, editable=True, default=r'{}')
    # attachment = models.FilePathField()

    def update(self, data:dict):
        self.name = data.get('name') if data.get('name') else self.name
        self.description = data.get('description') if data.get('description') else self.description
        self.date = data.get('date') if data.get('date') else self.date
        self.verified = data.get('verified') if data.get('verified') else self.verified
        self.place = data.get('place') if data.get('place') else self.place
        self.tag = data.get('tag') if data.get('tag') else self.tag
        self.save()

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

    def update(self, data: dict):
        self.user = data.get('user') if data.get('user') else self.user
        self.event = data.get('event') if data.get('event') else self.event
        self.comment = data.get('comment') if data.get('comment') else self.comment
        self.rating = data.get('rating') if data.get('rating') else self.rating
        self.save()

    def __str__(self) -> str:
        return f'{self.user} -> {self.event}'

