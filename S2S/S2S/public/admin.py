from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
	list_display = ['id','username']
	list_filter = ['username']
	search_fields = ['username']
	list_per_page = 10
	fields = ['username', 'first_name', 'last_name', 'password', 'phone', 'email', 'gender', 'dob', 'profile', 'activate', 'status', 'is_landlord']

class HouseAdmin(admin.ModelAdmin):
	list_display = ['id','name']
	list_filter = ['name']
	search_fields = ['name']
	list_per_page = 10
	fieldsets = [
		('Basic Information', {'fields': ['user_id','name','address','postcode','price','profile']}),
		('House detail', {'fields': ['max_guests', 'no_of_beds','no_of_bedrooms','no_of_baths','no_of_parking'
									 ,'tv','kitchen','washer','fridge','conditioner','wifi','study_room',
									 'pool']}),
		('Extra Description', {'fields': ['house_rule','cancellation','extra','status']})
	]


admin.site.register(User,UserAdmin)
admin.site.register(House,HouseAdmin)
