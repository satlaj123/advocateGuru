from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from prisonSol.models import *

# Create your models here.
class AdvocateUser(models.Model):
	user = models.OneToOneField(User,null = True,blank = True)
	mobile_number = models.CharField(max_length = 100,null = True,blank = True)
	middle_name = models.CharField(max_length = 200,null = True,blank = True)
	email = models.CharField(max_length = 100,null = True,blank = True)
	blood_group = models.ForeignKey(BloodGroupMaster,null = True ,blank = True,on_delete = models.CASCADE)
	aadhar_no = models.CharField(max_length = 100,null = True,blank = True)
	activationToken = models.CharField(max_length = 50,null = True,blank = True)
	activationAttempts = models.IntegerField(default = 0,null = True,blank = True)
	isProfileComplete = models.BooleanField(default = False)
	active_yesNo = models.BooleanField(default=False)
	last_modified_by = models.BigIntegerField(null = True, blank = True)
	last_modified_date_time = models.DateTimeField(auto_now_add = True, null = True, blank = True)
	# pTime = models.DateTimeField(null = True, blank = True)
	advocatePrison = models.ForeignKey(Registration, null = True, blank = True)

	class meta:
		db_table = 'advocateuser'

	def __str__(self):
		return '%s '%(self.email)

class AdvocateProfile(models.Model):
	advocateId = models.OneToOneField(AdvocateUser,on_delete = models.CASCADE,null = True,blank = True)
	dob = models.DateField(null = True,blank = True)
	# profilePhoto = models.URLField(null = True, blank = True)
	gender = models.ForeignKey(GenderMaster,on_delete = models.CASCADE,null = True,blank = True)
	country = models.ForeignKey(CountryMaster,on_delete=models.CASCADE, null = True, blank = True)
	state = models.ForeignKey(StateMaster,on_delete=models.CASCADE, null = True, blank = True)
	city = models.ForeignKey(CityMaster,on_delete=models.CASCADE, null = True, blank = True)
	address = models.CharField(max_length=100, null = True, blank = True)
	license_no = models.CharField(max_length = 100,null = True, blank = True)
	pincode = models.BigIntegerField(null = True,blank = True)

	def __str__(self):
		return '%s %s' %(self.advocateId.user.username,self.advocateId.email)

class AdvocateNotificationMaster(models.Model):
	advocateId = models.ForeignKey(AdvocateUser,on_delete=models.CASCADE,null = True, blank = True)
	notification_name = models.CharField(max_length = 200,null = True, blank = True)
	created_at = models.DateTimeField(null = True, blank = True)
	last_modified_date_time = models.DateTimeField(null = True, blank = True)
	isActiveYesNO = models.BooleanField(default = True)

	def __str__(self):
		return '%s %s' % (self.id,self.advocateId)


class AdvocateNotificationMaster_saver(models.Model):
	advocateId = models.ForeignKey(AdvocateUser,on_delete=models.CASCADE,null = True, blank = True)
	notification_name = models.CharField(max_length = 200,null = True, blank = True)
	created_at = models.DateTimeField(null = True, blank = True)
	last_modified_date_time = models.DateTimeField(null = True, blank = True)
	isActiveYesNO = models.BooleanField(default = True)
	notification_time = models.TimeField(null = True,blank = True)
	def __str__(self):
		return '%s %s' % (self.id,self.advocateId)


class ScheduleMaster(models.Model):
	doctorId = models.ForeignKey(AdvocateUser,on_delete=models.CASCADE,null = True ,blank = True)
	# day = models.ForeignKey(DayMaster,on_delete = models.CASCADE,null = True,blank = True)
	day = models.CharField(max_length = 100,null = True,blank = True)
	date = models.DateField(null = True, blank = True)
	from_time = models.TimeField(null = True, blank = True)
	to_time = models.TimeField(null = True, blank = True)
	venue = models.CharField(max_length = 100, null = True, blank = True)
	total_availability = models.IntegerField(null = True, blank = True)

	def __str__(self):
		return '%s %s' % (self.id,self.advocateId)

class AdvocateAppointmentsMaster(models.Model):
	mm = (('Confirmed',1),('Rejected',2),('Hold',3),('Pending',4))
	advocateId = models.ForeignKey(AdvocateUser,on_delete=models.CASCADE,null = True ,blank = True)
	prisonId = models.ForeignKey(Registration,on_delete=models.CASCADE,null = True ,blank = True)
	appointment_date_time = models.DateTimeField(null = True, blank = True)
	status = models.CharField(max_length = 20,choices = mm)
	venue_decided = models.ForeignKey(ScheduleMaster,on_delete=models.CASCADE,null=True,blank=True)
	isActiveYesNO = models.BooleanField(default = False)

	def __str__(self):
		return '%s %s' % (self.id,self.advocateId)

class SendMessage(models.Model):
	name = models.CharField(max_length = 100,null = True,blank = True)
	email = models.CharField(max_length = 50)
	subject = models.CharField(max_length = 100,null = True,blank = True)
	message = models.CharField(max_length = 300)

	class meta:
		db_table = 'sendmessage'

	def __str__(self):
		return '%s %s' %(self.id,self.email)
