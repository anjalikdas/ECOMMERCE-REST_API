from django.urls import path,include
from rest_framework import routers, urlpatterns
from rest_framework.viewsets import ViewSet
from . import views
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register('categoryapi',viewset=views.CategoryViewset,basename='category')
router.register('productapi',viewset=views.ProductViewset,basename='product')


urlpatterns=[
    path('',include(router.urls))
]