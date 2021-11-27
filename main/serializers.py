from rest_framework import serializers
from .models import Event, User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['uid', 'tg_uid', 'vk_uid', 'username', 'password']

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields =  ['id','name','description','date']