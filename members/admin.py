
from django.contrib import admin

from members.models import MemberDetails


class MemberDetailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone_number')

admin.site.register(MemberDetails, MemberDetailsAdmin)