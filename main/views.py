from django.core import exceptions
from django.http import HttpResponse, JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication 

from .models import User, Event, Subscription
from .serializers import EventSerializer, SubscriptionSerializer, UserSerializer

import json

class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
@authentication_classes((CsrfExemptSessionAuthentication, BasicAuthentication))
def users(request, token, id=None):
    
    if request.method == 'GET':
        if id:
            try:
                user = User.objects.get(id=id)
                serializer = UserSerializer(user, many=False)
                return JsonResponse(serializer.data, status=status.HTTP_200_OK)
            except User.DoesNotExist as ex:
                return JsonResponse({'error': str(ex)}, status=status.HTTP_404_NOT_FOUND)
        else:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
        
        return JsonResponse({'users': serializer.data, 'token':token}, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':

        data = request.data       
        if data:
            try:
                user = User()
                user.tg_uid = data.get('tg_uid')
                user.vk_uid = data.get('vk_uid')
                user.username = data.get('username')
                user.password = data.get('password')
                user.email = data.get('email')
                user.phone = data.get('phone')
                if data.get('pref_channel'):
                    user.pref_channel = data.get('pref_channel')
                if data.get('is_staff'):
                    user.is_staff = data.get('is_staff')
                
                if data.get('tags'):
                    user.add_tags(data.get('tags'))
                
                user.save()
            except Exception as ex:
                return JsonResponse(data={'error': str(ex)}, status=status.HTTP_400_BAD_REQUEST)
            
            return JsonResponse(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        
        return JsonResponse(data={'error':'Missing arguments!'}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        
        data = request.data
        
        if data:
            
            try:
                user = User.objects.get(id=data.get('id'))
               
                user.delete()
                
                return JsonResponse(data={}, status=status.HTTP_200_OK)
            
            except User.DoesNotExist as ex:
                return JsonResponse(data={'error':str(ex)}, status=status.HTTP_404_NOT_FOUND)
        
        else:
            return JsonResponse(data=data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST', 'GET'])
@authentication_classes((CsrfExemptSessionAuthentication, BasicAuthentication))
def edit_user(request, token, id):
    data = request.data
    if request.method == 'POST':
        try:
            user = User.objects.get(id=id)
            user.update(data)
            return JsonResponse(data=UserSerializer(user).data, status=status.HTTP_200_OK)
        except User.DoesNotExist as ex:
            return JsonResponse(data={'error':str(ex)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return JsonResponse(data={'error':str(ex)}, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        try:
            user = User.objects.get(id=id)
            return JsonResponse(data=UserSerializer(user).data, status=status.HTTP_200_OK)
        except User.DoesNotExist as ex:
            return JsonResponse(data={'error':str(ex)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return JsonResponse(data={'error':str(ex)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST', 'GET'])
@authentication_classes((CsrfExemptSessionAuthentication, BasicAuthentication))
def edit_event(request, token, id):
    data = request.data
    if request.method == 'POST':
        try:
            event = Event.objects.get(id=id)
            event.update(data)
            return JsonResponse(data=EventSerializer(event).data, status=status.HTTP_200_OK)
        except Event.DoesNotExist as ex:
            return JsonResponse(data={'error':str(ex)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return JsonResponse(data={'error':str(ex)}, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        try:
            event = Event.objects.get(id=id)
            return JsonResponse(data=EventSerializer(event).data, status=status.HTTP_200_OK)
        except Event.DoesNotExist as ex:
            return JsonResponse(data={'error':str(ex)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return JsonResponse(data={'error':str(ex)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST', 'GET'])
@authentication_classes((CsrfExemptSessionAuthentication, BasicAuthentication))
def edit_subscription(request, token, id):
    data = request.data
    if request.method == 'POST':
        try:
            sub = Subscription.objects.get(id=id)
            sub.update(data)
            return JsonResponse(data=SubscriptionSerializer(sub).data, status=status.HTTP_200_OK)
        except Subscription.DoesNotExist as ex:
            return JsonResponse(data={'error':str(ex)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return JsonResponse(data={'error':str(ex)}, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        try:
            sub = Subscription.objects.get(id=id)
            return JsonResponse(data=SubscriptionSerializer(sub).data, status=status.HTTP_200_OK)
        except Subscription.DoesNotExist as ex:
            return JsonResponse(data={'error':str(ex)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return JsonResponse(data={'error':str(ex)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
@authentication_classes((CsrfExemptSessionAuthentication, BasicAuthentication))
#/users/<id>/subscribe/<event_id>
#/users/<event_id>/subscribe/<id>
def subscribe_user(request, token, id, event_id=None):
    
    if request.method == 'GET':
        if event_id:
            try:
                user = User.objects.get(id=id)
                event = Event.objects.get(id=event_id)
                user.subscribe(event)
                return JsonResponse(data={}, status=status.HTTP_200_OK)
            except User.DoesNotExist as ex:
                return JsonResponse(data={'error':str(ex)}, status=status.HTTP_404_NOT_FOUND)
            except Event.DoesNotExist as ex:
                return JsonResponse(data={'error':str(ex)}, status=status.HTTP_404_NOT_FOUND)
            except Exception as ex:
                return JsonResponse(data={'error':str(ex)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                user = User.objects.get(id=id)
                subs = user.get_subscriptions()
                return JsonResponse(data={'user':UserSerializer(user).data,'subscriptions':SubscriptionSerializer(subs,many=True)}, status=status.HTTP_200_OK)
            except User.DoesNotExist as ex:
                return JsonResponse(data={'error':str(ex)}, status=status.HTTP_404_NOT_FOUND)
            except Exception as ex:
                return JsonResponse(data={'error':str(ex)}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'POST':
        if event_id:
            try:
                user = User.objects.get(id=id)
                event = Event.objects.get(id=event_id)
                user.subscribe(event)
                return JsonResponse(data={}, status=status.HTTP_200_OK)
            except User.DoesNotExist as ex:
                return JsonResponse(data={'error':str(ex)}, status=status.HTTP_404_NOT_FOUND)
            except Event.DoesNotExist as ex:
                return JsonResponse(data={'error':str(ex)}, status=status.HTTP_404_NOT_FOUND)
            except Exception as ex:
                return JsonResponse(data={'error':str(ex)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                data = request.data
                if data.get('event_id'):
                    user = User.objects.get(id=id)
                    event = Event.objects.get(id=data.get('event_id'))
                    user.subscribe(event)
                    return JsonResponse(data={}, status=status.HTTP_200_OK)
                else:
                    return JsonResponse(data={'error': 'Missing argument event_id'}, status=status.HTTP_400_BAD_REQUEST)
            except User.DoesNotExist as ex:
                return JsonResponse(data={'error':str(ex)}, status=status.HTTP_404_NOT_FOUND)
            except Event.DoesNotExist as ex:
                return JsonResponse(data={'error':str(ex)}, status=status.HTTP_404_NOT_FOUND)
            except Exception as ex:
                return JsonResponse(data={'error':str(ex)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST','DELETE'])
@authentication_classes((CsrfExemptSessionAuthentication, BasicAuthentication))
def subscriptions(request, token, id=None):
    
    if request.method == 'GET':

        if id:
            try:
                sub = Subscription.objects.get(id=id)
                serializer = SubscriptionSerializer(sub, many=False)
                return JsonResponse(serializer.data, status=status.HTTP_200_OK)
            except Subscription.DoesNotExist as ex:
                return JsonResponse({'error': str(ex)}, status=status.HTTP_404_NOT_FOUND)
        else:
            subs = Subscription.objects.all()
            serializer = SubscriptionSerializer(subs, many=True)
        
        return JsonResponse({'subscriptions':serializer.data, 'token':token})

    elif request.method == 'POST':
        
        data = request.data       
        if data:
            try:
                subscription = Subscription()
                user = User.objects.get(id=data.get('user_id'))
                subscription.user = user
                event = Event.objects.get(id=data.get('event_id'))
                subscription.event = event                            

                subscription.save()
                
                return Response(SubscriptionSerializer(subscription).data, status=status.HTTP_201_CREATED)
            except exceptions.ValidationError as ex:
                return Response(data=str(ex), status=status.HTTP_400_BAD_REQUEST)
            except User.DoesNotExist as ex:
                return Response(data=str(ex), status=status.HTTP_404_NOT_FOUND)
            except Event.DoesNotExist as ex:
                return Response(data=str(ex), status=status.HTTP_404_NOT_FOUND)

        
        return Response(data, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':

        data = request.data
        
        if data:
            
            try:
                sub = Subscription.objects.get(id=data.get('id'))
                sub.delete()
                
                return Response(data={}, status=status.HTTP_302_FOUND)
            
            except Subscription.DoesNotExist as ex:
                return Response(data=str(ex), status=status.HTTP_404_NOT_FOUND)
        
        else:
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST', 'DELETE'])
@authentication_classes((CsrfExemptSessionAuthentication, BasicAuthentication))
def events(request, token, id=None):
    
    if request.method == 'GET':
        
        if id:
            try:
                event = Event.objects.get(id=id)
                serializer = EventSerializer(event, many=False)
                return JsonResponse(serializer.data, status=status.HTTP_200_OK)
            except Event.DoesNotExist as ex:
                return JsonResponse({'error': str(ex)}, status=status.HTTP_404_NOT_FOUND)
        else:
            events = Event.objects.all()
            serializer = EventSerializer(events, many=True)
        
        return JsonResponse({'events':serializer.data, 'token':token})
    
    elif request.method == 'POST':
        
        data = request.data       
        if data:
            try:
                event = Event()
                event.name = data.get('name')
                event.description = data.get('description')
                event.date = data.get('date')
                event.place = data.get('place')
                if data.get('verified'):
                    event.verified = data.get('verified')
                if data.get('tags'):
                    event.add_tags(data.get('tags'))
                            
                event.save()
                
                return Response(EventSerializer(event).data, status=status.HTTP_201_CREATED)
            except exceptions.ValidationError as ex:
                return Response(data=str(ex), status=status.HTTP_400_BAD_REQUEST)
        
        return Response(data, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':

        
        data = request.data
        
        if data:
            
            try:
                event = Event.objects.get(id=data.get('id'))
                event.delete()
                
                return Response(data={}, status=status.HTTP_302_FOUND)
            
            except Event.DoesNotExist as ex:
                return Response(data=str(ex), status=status.HTTP_404_NOT_FOUND)
        
        else:
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

def index(request):
    return HttpResponse("Hello world!")

