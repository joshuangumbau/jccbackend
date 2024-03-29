from calendar import monthrange
import datetime
import random
from django.http import JsonResponse
from django.shortcuts import render
from django.db import transaction
from accounts.models import AccountModel
import requests
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from rest_framework.decorators import (api_view, parser_classes,
                                       permission_classes)
from rest_framework.parsers import JSONParser,MultiPartParser,FormParser

from rest_framework.exceptions import NotFound

from dateutil.parser import parse

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import json
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import api_view,permission_classes
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated,AllowAny

# from members.utilis import convert_phone
from lipanampesa.models import MpesaPayment
from lipanampesa.serializers import MpesaSerializer





class MpesaCallBack(APIView):
    permission_classes = [AllowAny,]

    def get(self, request):
        obj = MpesaPayment.objects.all().order_by('-created')
        serializer = MpesaSerializer(obj, many=True)
        return Response({"status": True, "data": serializer.data})
   

    def post(self, request):
        request_data = json.dumps(request.data)
        data = json.loads(request_data)
        created=MpesaPayment.objects.create(
             phone_number=data['source']['msisdn'],
             email=data['source']['owner_email'],
             amount=data['transaction']['amount'],
             receipt_code =data['transaction']['receipt'],
             channel=data['transaction']['channel'],
             callback_id=data['transaction']['id'],
             charge_id=data['charge_id'],
             status=data['status'],
            
             status_code=data['status_code'],
             date=datetime.datetime.now().date()
                      )
        try:
            created.json_response=data
            created.save()
        except:
             pass

  
        return Response(status=200) 
