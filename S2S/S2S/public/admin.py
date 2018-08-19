from django.contrib import admin
from .models import *

class TenantAdmin(admin.ModelAdmin):
	list_display = ['id','username']

class LandLordAdmin(admin.ModelAdmin):
	list_display = ['id','username']

class HouseAdmin(admin.ModelAdmin):
	list_display = ['id','name']


admin.site.register(Tenant,TenantAdmin)
admin.site.register(Landlord,LandLordAdmin)
admin.site.register(House,HouseAdmin)
