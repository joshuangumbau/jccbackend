from django.urls import path,include

from rest_framework import routers

from members.sms import SMS

from .views import *
from . import views
from rest_framework.routers import DefaultRouter
rs=DefaultRouter()
urlpatterns = [      
        path('create-new-member-detail/',CreateDetailAPIView.as_view()),
        
        path('',include(rs.urls)), 
        
        
        ]