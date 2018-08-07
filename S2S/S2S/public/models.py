from django.db import models

# Create your models here.
class Tenant(models.Model):
	username = models.CharField(max_length=64, null=False)
	password = models.CharField(max_length=256, null=False)
	email = models.EmailField(null=False)
	profile = models.TextField(null=True, blank=False)
	activatied = models.BooleanField(default=False)
	time_stamp = models.DateTimeField(auto_now_add = True)
	tag = models.CharField(max_length =64, null=True, blank=True)

	class Meta:
		db_table = "tenant"

	def __str__(self):
		return self.username

class Landlord(models.Model):
	username = models.CharField(max_length=64, null=False)
	password = models.CharField(max_length=256, null=False)
	email = models.EmailField(null=False)
	profile = models.TextField(null=True, blank=False)
	activatied = models.BooleanField(default=False)
	time_stamp = models.DateTimeField(auto_now_add = True)
	tag = models.CharField(max_length =64, null=True, blank=True)

	class Meta:
		db_table = "landlord"

	def __str__(self):
		return self.username

class House(models.Model):
	housename = models.CharField(max_length=256, null=False)
	address = models.CharField(max_length=256, null=False)
	postcode = models.IntegerField(null=True)

	class Meta:
		db_table = "house"

	def __str__(self):
		return self.username