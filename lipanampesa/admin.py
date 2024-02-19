from django.contrib import admin

from lipanampesa.models import MpesaPayment


class MpesaPaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'amount', 'email', 'date')

admin.site.register(MpesaPayment, MpesaPaymentAdmin)