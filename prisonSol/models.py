from __future__ import unicode_literals
import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CountryMaster(models.Model):
	name = models.CharField(max_length=50)
	activeYesNo = models.BooleanField(default=False)
	lastModifiedDateTime = models.CharField(max_length=50, null = True, blank = True)
	def __str__(self):
		return '%s' % (self.name)

class StateMaster(models.Model):
	name = models.CharField(max_length=30)
	country = models.ForeignKey(CountryMaster,on_delete=models.CASCADE)
	activeYesNo = models.BooleanField(default=False)
	lastModifiedDateTime = models.CharField(max_length=50, null = True, blank = True)
	def __str__(self):
		return '%s' % (self.name)

class CityMaster(models.Model):
	name = models.CharField(max_length=30)
	state = models.ForeignKey(StateMaster,on_delete=models.CASCADE)
	activeYesNo = models.BooleanField(default=False)
	lastModifiedDateTime = models.CharField(max_length=50, null = True, blank = True)
	def __str__(self):
		return '%s' % (self.name)

class GenderMaster(models.Model):
	name = models.CharField(max_length = 20)
	lastDateTimeModified = models.DateTimeField()
	lastModifiedBy = models.CharField(max_length = 100)

	class meta:
		db_table = 'gendermaster'
	def __str__(self):
		return '%s %s' %(self.id,self.name)

class BloodGroupMaster(models.Model):
	name = models.CharField(max_length = 30)
	lastModifiedDateTime = models.CharField(max_length = 30, null = True, blank = True)
	activeYesNo = models.BooleanField(default=False)

	class meta:
		db_table = 'bloodgroupmaster'
	def __str__(self):
		return'%s' % (self.id)


class Registration(models.Model):
	user = models.OneToOneField(User,null = True,blank = True)
	first_name = models.CharField(max_length = 100,null = True,blank = True)
	last_name = models.CharField(max_length = 100,null = True,blank = True)
	middle_name = models.CharField(max_length =100, null = True,blank = True)
	gender = models.ForeignKey(GenderMaster,on_delete = models.CASCADE,null = True,blank = True)
	mobile_number = models.BigIntegerField()
	email = models.CharField(max_length = 50)
	image = models.ImageField(upload_to = 'proifle_image',blank = True )
	blood_group = models.ForeignKey(BloodGroupMaster,null = True,blank = True,on_delete = models.CASCADE)
	aadhar_no = models.BigIntegerField()
	country = models.ForeignKey(CountryMaster,null = True,blank = True,on_delete = models.CASCADE)
	state = models.ForeignKey(StateMaster,null = True, blank = True,on_delete = models.CASCADE)
	city = models.ForeignKey(CityMaster,null = True,blank = True,on_delete =models.CASCADE)
	date_of_birth = models.DateField(null = True,blank = True)
	activationToken = models.CharField(max_length = 20,null = True,blank = True)
	pincode = models.BigIntegerField(null = True,blank = True)
	address = models.CharField(max_length = 100,null = True,blank = True)
	# activationAttempts = models.IntegerField(default =0,null = True,blank = True)
	isProfileComplete = models.BooleanField(default = False)
	activeYesNo = models.BooleanField(default = False)
	lastModifiedDateTime = models.DateTimeField(auto_now_add = True,null = True,blank = True)

	class meta:
		db_table = 'registration'

	def __str__(self):
		return '%s %s' %(self.user.username,self.email)

class PrisonNotificationMaster(models.Model):
	prisonId = models.ForeignKey(Registration,null= True,blank=True,on_delete = models.CASCADE)
	notification_type_id = models.CharField(max_length = 100,null = True,blank = True)
	notification_type = models.CharField(max_length = 100,null = True,blank = True)
	notification_name = models.CharField(max_length = 100,null = True,blank = True)
	created_at = models.DateTimeField(auto_now_add = True,null = True,blank = True)
	last_modified_date_time = models.DateTimeField(auto_now_add = True,null = True,blank = True)
	isActiveYesNo = models.BooleanField(default = True)

	def __str__(self):
		return '%s %s'%(self.id, self.prisonId)

class PrisonNotificationMaster_saver(models.Model):
	prisonId = models.ForeignKey(Registration,null= True,blank=True,on_delete = models.CASCADE)
	notification_type_id = models.CharField(max_length = 100,null = True,blank = True)
	notification_type = models.CharField(max_length = 100,null = True,blank = True)
	notification_name = models.CharField(max_length = 100,null = True,blank = True)
	created_at = models.DateTimeField(auto_now_add = True,null = True,blank = True)
	last_modified_date_time = models.DateTimeField(auto_now_add = True,null = True,blank = True)
	isActiveYesNo = models.BooleanField(default = True)
	notification_time = models.TimeField(auto_now_add = True,null = True,blank = True)

	def __str__(self):
		return '%s %s'%(self.id, self.prisonId)

class PrisonAppointmentsMaster(models.Model):
	mm = (('Confirmed', 1),('Rejected',2),('Pending',3))
	advocateId = models.CharField(max_length = 100,null = True, blank = True)
	prisonId = models.ForeignKey(Registration,null = True,blank = True,on_delete = models.CASCADE)
	appointment_date_time = models.DateTimeField(auto_now_add = True,null= True,blank = True)
	status = models.CharField(max_length = 50,choices = mm)
	isActiveYesNo = models.BooleanField(default = True)

	def __str__(self):
		return  '%s %s' % (self.id,self.prisonId)