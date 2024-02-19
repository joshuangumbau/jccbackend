from rest_framework import serializers
from lipanampesa.models import MpesaPayment

class MpesaSerializer(serializers.ModelSerializer):
    class Meta:  # Capital "M" for Meta
        model = MpesaPayment
        fields = '__all__'  # Correct usage of '__all__'
