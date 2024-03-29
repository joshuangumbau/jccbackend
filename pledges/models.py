from django.db import models

from django.conf import settings
from django.db.models import CASCADE
class Member(models.Model):
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    
class Pledge(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    date_created = models.DateTimeField(auto_now_add = True)