from rest_framework import serializers
from .models import Event, Subscription, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'tg_uid', 'vk_uid', 'username', 'password']

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields =  ['id','name','description','date']

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['id', 'user', 'event']