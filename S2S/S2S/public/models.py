from django.db import models

# Create your models here.
class User(models.Model):
	gender_choices = (('M','Male'),('F','Female'),)
	time_stamp = models.DateTimeField(auto_now_add=True)
	username = models.CharField(max_length=64, null=False)
	first_name = models.CharField(max_length=64, null=True)
	last_name = models.CharField(max_length=64, null=True)
	password = models.CharField(max_length=256, null=False)
	email = models.EmailField(null=False)
	phone = models.CharField(max_length=128, null=True)
	photo = models.ImageField(upload_to='user', default='user/default.png', blank=True)
	gender = models.CharField(max_length=1, choices=gender_choices, default='M')
	dob = models.DateField(null=True,auto_now=False, auto_now_add=False)
	profile = models.TextField(null=True, blank=True)
	activate = models.BooleanField(default=False)
	status = models.BooleanField(default=True)
	is_landlord = models.BooleanField(default=False)

	class Meta:
		db_table = "user"

	def __str__(self):
		return self.username


class House(models.Model):
	time_stamp = models.DateTimeField(auto_now_add=True)
	user_id = models.IntegerField(null=False)
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
	extra = models.TextField(null=True, blank=True)
	status = models.BooleanField(default=True)

	class Meta:
		db_table = "house"

	def __str__(self):
		return self.name

class House_Picture(models.Model):
	time_stamp = models.DateTimeField(auto_now_add=True)
	house_id = models.IntegerField(null=False)
	photo = models.ImageField(upload_to='house', null=False)

	def __str__(self):
		return self.house_id

	class Meta:
		db_table = "house_picture"

class Lease_Period(models.Model):
	time_stamp = models.DateTimeField(auto_now_add=True)
	house_id = models.IntegerField(null=False)
	period_start = models.DateField(null=False)
	period_end = models.DateField(null=False)

	def __str__(self):
		return self.house_id

	class Meta:
		db_table = "lease_period"

class Tag(models.Model):
	time_stamp = models.DateTimeField(auto_now_add=True)
	tag = models.CharField(max_length=64, null=False)

	def __str__(self):
		return self.tag

	class Meta:
		db_table = "tag"

class User_Tag(models.Model):
	time_stamp = models.DateTimeField(auto_now_add=True)
	user_id = models.IntegerField(null=False)
	tag_id = models.IntegerField(null=False)

	def __str__(self):
		return self.tenant_id

	class Meta:
		db_table = "tenant_tag"

class House_Tag(models.Model):
	time_stamp = models.DateTimeField(auto_now_add=True)
	house_id = models.IntegerField(null=False)
	tag_id = models.IntegerField(null=False)

	def __str__(self):
		return self.house_id

	class Meta:
		db_table = "house_tag"

class User_Rate(models.Model):
	time_stamp = models.DateTimeField(auto_now_add=True)
	# user1 is tenant, user2 is landlord
	user1_id = models.IntegerField(null=False)
	user2_id = models.IntegerField(null=False)
	reputation = models.IntegerField(null=False)

	def __str__(self):
		return self.tenant_id

	class Meta:
		db_table = "tenant_rate"

class House_Rate(models.Model):
	time_stamp = models.DateTimeField(auto_now_add=True)
	user_id = models.IntegerField(null=False)
	house_id = models.IntegerField(null=False)
	accuracy = models.IntegerField(null=False)
	communication = models.IntegerField(null=False)
	cleanliness = models.IntegerField(null=False)
	location = models.IntegerField(null=False)
	check_in = models.IntegerField(null=False)
	value = models.IntegerField(null=False)

	def __str__(self):
		return self.house_id

	class Meta:
		db_table = "house_rate"

class House_Comment(models.Model):
	time_stamp = models.DateTimeField(auto_now_add=True)
	user_id = models.IntegerField(null=False)
	house_id = models.IntegerField(null=False)
	comment = models.TextField(null=False, blank=False)

	def __str__(self):
		return self.house_id

	class Meta:
		db_table = "house_comment"
