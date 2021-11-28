from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('api/<str:token>/users/', views.users, name='users by api'),
    path('api/<str:token>/users/<str:id>', views.users, name='users by api'),
    path('api/<str:token>/users/<str:id>/edit', views.edit_user, name='users by api'),
    path('api/<str:token>/users/<str:id>/subscribe', views.subscribe_user, name='users by api'),
    path('api/<str:token>/users/<str:id>/subscribe/<str:event_id>', views.subscribe_user, name='users by api'),
    path('api/<str:token>/events/', views.events, name='events by api'),
    path('api/<str:token>/events/<str:id>', views.events, name='events by api'),
    path('api/<str:token>/subs/', views.subscriptions, name='events by api'),
    path('api/<str:token>/subs/<str:id>', views.subscriptions, name='events by api'),
]
