from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('api/<str:token>/users/', views.users, name='users by api'),
    path('api/<str:token>/users/<str:uid>', views.users, name='users by api'),
    path('api/<str:token>/events/', views.events, name='events by api')
]
