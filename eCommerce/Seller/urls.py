from django.conf.urls import url
from django.urls import path,include
from rest_framework import routers, urlpatterns
from rest_framework import viewsets
from rest_framework.viewsets import ViewSet
from . import views
from rest_framework_extensions.routers import ExtendedDefaultRouter


router =  ExtendedDefaultRouter()

(router.register('company',viewset=views.CompanyViewset,basename='company').register('employee',viewset=views.EmployeeViewset,basename='company-employee',parents_query_lookups=['Company'],))

router.register('employee_detail',viewset=views.EmployeeDetailViewset,basename='employee-detail')

urlpatterns = [
    path('',include(router.urls)),
    path('department/',views.DepartmentList.as_view(),name='department'),
    
    
    
]