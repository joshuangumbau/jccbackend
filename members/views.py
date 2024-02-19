import random
from django.shortcuts import render

# Create your views here.
import dataclasses
from datetime import datetime
from django.shortcuts import render
from rest_framework import permissions
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import (api_view, parser_classes,
                                       permission_classes)
from rest_framework.parsers import JSONParser,MultiPartParser,FormParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_302_FOUND, HTTP_400_BAD_REQUEST
from accounts.models import AccountModel
from members.models import  CustomerOrder, Policies
from members.serializer import CustomerListSerializer, policyListSerializer
from dateutil.relativedelta import relativedelta
from dateutil.parser import parse
import africastalking                                                                                                                                                                                          

class CreateDetailAPIView(APIView):
    parser_classes=(JSONParser,FormParser,MultiPartParser)
    permission_classes=[IsAuthenticated]
    def get(self,request):
        data=request.data
        query=CustomerOrder.objects.all()
        dt=CustomerListSerializer(query).data
        rep_data={
                "status":True,
                "message":"Taxes Fethed Successfully",
                "object":dt
            }
        return Response(rep_data,status=200)