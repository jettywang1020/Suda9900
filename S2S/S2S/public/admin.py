from django.contrib import admin
from .models import *

class TenantAdmin(admin.ModelAdmin):
	list_display = ['id','username']
	list_filter = ['username']
	search_fields = ['username']
	list_per_page = 10
	fields = ['username','password','phone','email','gender','dob','profile','activate','status']

class LandLordAdmin(admin.ModelAdmin):
	list_display = ['id','username']
	list_filter = ['username']
	search_fields = ['username']
	list_per_page = 10
	fields = ['username', 'password', 'phone', 'email', 'gender', 'dob', 'profile', 'activate', 'status']

class HouseAdmin(admin.ModelAdmin):
	list_display = ['id','name']
	list_filter = ['name']
	search_fields = ['name']
	list_per_page = 10
	fieldsets = [
		('Basic Information', {'fields': ['landlord_id','name','address','postcode','price','profile']}),
		('House detail', {'fields': ['bpub_date', 'bpub1_date']}),
	]


admin.site.register(Tenant,TenantAdmin)
admin.site.register(Landlord,LandLordAdmin)
admin.site.register(House,HouseAdmin)
