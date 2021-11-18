from django.urls import path,include
from rest_framework import routers, urlpatterns
from rest_framework.viewsets import ViewSet
from . import views
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register('Productcart',viewset=views.ProductCartViewset,basename='productcart')
router.register('OrderApi',viewset=views.OrderViewset,basename='order')
router.register('Ordereddate',viewset=views.OrdereddateViewset,basename='ordereddate')


urlpatterns=[
    path('',include(router.urls)),
    path('productdetail/',views.ProductDetail.as_view(),name='productdetail'),
    path('ordered_date',views.OrderedDateView.as_view())
]