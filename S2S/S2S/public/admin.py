from django.contrib import admin
from .models import *

class TenantAdmin(admin.ModelAdmin):
	list_display = ['id','username','email']

class LandLordAdmin(admin.ModelAdmin):
	list_display = ['id','username','email']

admin.site.register(Tenant,TenantAdmin)
admin.site.register(Landlord,LandLordAdmin)
