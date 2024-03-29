from django.db import models
import uuid


import members
class MemberDetails(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4)
    phone_number = models.CharField(max_length=100, null=True, blank=True)

class Payment(models.Model):
    # member = models.ForeignKey(members, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    date_paid = models.DateTimeField(auto_now_add=True)

