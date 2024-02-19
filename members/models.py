from django.db import models
import uuid

# Create your models here.
class MemberDetails(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4)
    created=models.DateTimeField(auto_now_add=True)