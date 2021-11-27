from django.core import exceptions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.http import HttpResponse, JsonResponse

from .models import User, Event, Subscription
from .serializers import EventSerializer, SubscriptionSerializer, UserSerializer

# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def users(request, token, uid=None):
    
    if request.method == 'GET':
        if uid:
            try:
                user = User.objects.get(uid=uid)
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
            
            user = User()
            user.uid = data.get('uid')
            user.tg_uid = data.get('tg_uid')
            user.vk_uid = data.get('vk_uid')
            user.username = data.get('username')
            user.password = data.get('password')
            
            # if data.get('tag'):
            #     user.add_tag(data.get('tag'))
            
            user.save()
            
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        
        return Response(data, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        
        data = request.data
        
        if data:
            
            try:
                if data.get('pk'):
                    user = User.objects.get(pk=data.get('pk'))
                elif data.get('uid'):
                    user = User.objects.get(uid=data.get('uid'))
               
                user.delete()
                
                return Response(data={}, status=status.HTTP_302_FOUND)
            
            except User.DoesNotExist as ex:
                return Response(data=str(ex), status=status.HTTP_404_NOT_FOUND)
        
        else:
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def subscribe_user(request, token, uid, event_id=None):
    
    if event_id:
        try:
            user = User.objects.get(uid=uid)
            event = Event.objects.get(id=event_id)
            user.subscribe(event)
            return Response(data={}, status=status.HTTP_200_OK)
        except Exception as ex:
            return Response(data=str(ex), status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST','DELETE'])
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

