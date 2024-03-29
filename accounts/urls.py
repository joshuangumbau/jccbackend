from django.urls import path,include

from rest_framework import routers

from .views import *
from . import views
from rest_framework.routers import DefaultRouter
rs=DefaultRouter()
urlpatterns = [
        path('login/',login), 
        path('reset_password/',ResetPasswordAPIView.as_view()),
        

        path('',include(rs.urls)), 
       
]
