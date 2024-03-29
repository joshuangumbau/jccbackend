import random
from django.shortcuts import render

import dataclasses
from datetime import datetime
from django.shortcuts import render
from accounts.serializer import  LoginSerializer, UserLoginSerializer
from rest_framework import permissions
from rest_framework.views import APIView

from .models import AccountModel
from django.shortcuts import get_object_or_404

from rest_framework import status, viewsets
from rest_framework.decorators import (api_view, parser_classes,
                                       permission_classes)
from rest_framework.parsers import JSONParser,MultiPartParser,FormParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_302_FOUND, HTTP_400_BAD_REQUEST


from django.core.mail import EmailMultiAlternatives

@api_view(['POST'])
@permission_classes((AllowAny,))
@parser_classes((JSONParser,FormParser,MultiPartParser ))
def login(request):
    data = request.data
    
    print(data)
    serializer = LoginSerializer(data=data, context={'request': request})
    if not serializer.is_valid():
        return Response({'error': 'blank username or password'}, status=401)
    user = get_object_or_404(AccountModel,email=serializer.validated_data['email'])
    if not user.check_password(serializer.validated_data['password']):
        return Response({'error': 'Incorrect username or password'}, status=401)
    serializer = UserLoginSerializer(user)
   
    data = serializer.data
   
    login_time=datetime.now()
   
    obj=AccountModel.objects.get(email=user.email)
   
    
    obj.last_login==login_time
    obj.save()
    return Response(data)

class ResetPasswordAPIView(APIView):
    parser_classes=(JSONParser,FormParser,MultiPartParser)
    permission_classes=[AllowAny]
    def post(self,request):
        data = request.data
        print(data)
        try:
                accountModel=AccountModel.objects.filter(is_archive=False).get(email=data['email'])
                if  accountModel != None:
                        
                        val="IBS"+str(random.randint(10000,10000000))
                        passwordreset=val
                        subject, from_email, to = 'Password Reset Details', 'thebhubinfor@gmail.com',data['email']
                        accountModel.set_password(passwordreset)
                        print(passwordreset)
                        accountModel.save()
                        text_content = ''
                        html_content = """
                        <h4>Hi  """ +accountModel.email+""" </h4>
                        <div style="margin-left:5px;font-size:12px">
                        You have successfully Reset your account for the IBS system <a href="https://ibs/bhub/#/login">https://ibs/bhub/#/login</a> <br>
                        Below are your Credentials.<br>
                        <b>Username</b>: """+accountModel.email+"""<br>
                        <b>Password</b>:"""+str(passwordreset)+"""
                        <br>
                        <br>
                        Please Login Using the Above Credentials,<br>
                        You can Opt to Reset Your preffered Password  on the Dashboard after Login.<br>
                        </div>

                        <div>
                        Regards,<br>
                        Bhub Support,<br>
                        
                        </div>
                        """
                        print("tunaanza")
                        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                        msg.attach_alternative(html_content, "text/html")
                        print("sending....")
                        # print("from":from)
                        msg.send()
                        return Response({"success":"Password Reset Successfull"},status=HTTP_200_OK)
                    
                return Response({"error":"Passwords does not match"},status=HTTP_400_BAD_REQUEST)
        except:
            return Response({"status":False,"error":"user with that email does not exist"})
