
from django.contrib import admin

from .models import Member,Pledge

class PledgeAdmin(admin.ModelAdmin):
    list_display = ('member', 'target_amount', 'amount_paid', 'date_created') 
    list_filter = ('date_created', )

admin.site.register(Member)
admin.site.register(Pledge, PledgeAdmin)