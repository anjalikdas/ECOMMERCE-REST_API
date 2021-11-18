from django.urls import path,include
from rest_framework import routers, urlpatterns
from rest_framework.viewsets import ViewSet
from . import views
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register('customer',viewset=views.CustomerViewset,basename='customer')
router.register('user',viewset=views.UserViewset,basename='user')



urlpatterns=[
    path('',include(router.urls)),
    path('state/',views.StateList.as_view(),name='state'),
]