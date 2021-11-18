from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register('payment',viewset=views.PaymentViewset,basename='payment')
router.register('sucessful',viewset=views.Successfull_transactionViewset,basename='sucessful_transaction-detail')
router.register('unsucessful_transaction',viewset=views.Unsuccessfull_transactionViewset,basename='unsucessful')


urlpatterns=[
    path('',include(router.urls)),
    path('customer/',views.Customer_spending.as_view(),name='cust'),
]