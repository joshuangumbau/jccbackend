from django.db import models
from django.db.models import JSONField
import uuid

class MpesaPayment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    receipt_code = models.CharField(max_length=100, null=True, blank=True, unique=True)
    date = models.DateTimeField(null=True, blank=True)
    reference = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=100, null=True, blank=True)
    charge_id = models.CharField(max_length=100, null=True, blank=True)
    callback_id = models.CharField(max_length=100, null=True, blank=True)
    channel = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    status_code = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=100, null=True, blank=True)

    is_utilized = models.BooleanField(default=False)
    # json_response = JSONField(null=True, blank=True, default={})  # Changed default value to dictionary
    json_response = models.JSONField(default=dict) 

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Mpesa Payment'
        verbose_name_plural = 'Mpesa Payments'

    def __str__(self):
        return self.receipt_code if self.receipt_code else ''
    
from django.db import models
import uuid

class PushedSTKs(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    channel = models.CharField(max_length=100)
    reference = models.CharField(max_length=100)
    mechant_app_id = models.CharField(max_length=100)
    uuid = models.CharField(max_length=100)
    stk_id = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Pushed STK'
        verbose_name_plural = 'Pushed STKs'

    def __str__(self):
        return self.reference

