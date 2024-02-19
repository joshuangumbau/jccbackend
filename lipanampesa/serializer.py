import json
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from lipanampesa.models import MpesaPayment

class MpesaSerializer(serializers.ModelSerializer):

    class meta: 
        model = MpesaPayment
        fields = ('__all__')