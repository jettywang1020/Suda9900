from django.db import models

# Create your models here.
class Tenant(models.Model):
	time_stamp = models.DateTimeField(auto_now_add=True)
	username = models.CharField(max_length=64, null=False)
	password = models.CharField(max_length=256, null=False)
	phone = models.CharField(max_length=128, null=False)
	email = models.EmailField(null=False)
	photo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
	gender = models.BooleanField(default=False)
	dob = models.DateField()
	profile = models.TextField(null=True, blank=False)
	activate = models.BooleanField(default=False)
	status = models.BooleanField(default=True)

	class Meta:
		db_table = "tenant"

	def __str__(self):
		return self.username

class Landlord(models.Model):
	time_stamp = models.DateTimeField(auto_now_add=True)
	username = models.CharField(max_length=64, null=False)
	password = models.CharField(max_length=256, null=False)
	phone = models.CharField(max_length=128, null=False)
	email = models.EmailField(null=False)
	photo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
	gender = models.BooleanField(default=False)
	dob = models.DateField()
	profile = models.TextField(null=True, blank=False)
	activate = models.BooleanField(default=False)
	status = models.BooleanField(default=True)

	class Meta:
		db_table = "landlord"

	def __str__(self):
		return self.username

class House(models.Model):
	time_stamp = models.DateTimeField(auto_now_add=True)
	landord_id = models.IntegerField(null=False)
	name = models.CharField(max_length=256, null=False)
	address = models.CharField(max_length=256, null=False)
	postcode = models.IntegerField(null=False)
	price = models.IntegerField(null=False)
	profile = models.TextField(null=True, blank=False)
	max_guests = models.IntegerField(null=False)
	no_of_beds = models.IntegerField(null=False)
	no_of_bedrooms = models.IntegerField(null=False)
	no_of_baths = models.IntegerField(null=False)
	no_of_parking = models.IntegerField(null=False)
	tv = models.BooleanField(default=False)
	kitchen = models.BooleanField(default=False)
	washer = models.BooleanField(default=False)
	fridge = models.BooleanField(default=False)
	conditioner = models.BooleanField(default=False)
	wifi = models.BooleanField(default=False)
	study_room = models.BooleanField(default=False)
	pool = models.BooleanField(default=False)
	house_rule = models.TextField(null=False, blank=False)
	cancellation = models.TextField(null=False, blank=False)
	extra = models.TextField(null=True, blank=False)
	status = models.BooleanField(default=True)

	class Meta:
		db_table = "house"

	def __str__(self):
		return self.housename


class House_Comment(models.Model):
	time_stamp = models.DateTimeField(auto_now_add=True)
	tenant_id = models.IntegerField(null=False)
	house_id = models.IntegerField(null=False)
	comment = models.TextField(null=False, blank=False)

	class Meta:
		db_table = "house_comment"
