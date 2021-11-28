from rest_framework import serializers
from .models import Event, Subscription, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'tg_uid', 'vk_uid', 'username', 'password','email', 'phone', 'tags', 'pref_channel', 'is_staff']

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields =  ['id','name','description','date', 'place', 'verified', 'tags']

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['id', 'user', 'event', 'comment', 'rating']