from django.urls import path,include

from rest_framework import routers
from . import views
from rest_framework.routers import DefaultRouter
rs=DefaultRouter()
urlpatterns = [
    path('mpesapayments/callback/', views.MpesaCallBack.as_view(), name='MpesaCallBack'),
    path('', include(rs.urls)),
]
