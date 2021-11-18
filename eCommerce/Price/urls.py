from django.db import router
from django.urls import path,include
from rest_framework.viewsets import ViewSet
from . import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('productprice',views.ProductPriceViewset,basename='productprice')

urlpatterns = [
    path('',include(router.urls))
]
