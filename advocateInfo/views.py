from django.shortcuts import render_to_response, render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from random import randint
from .models import *
from prisonSol.models import *

# Create your views here.
def advo_register_show(request):
	countryObjects = CountryMaster.objects.all()
	stateObjects = StateMaster.objects.all()
	cityObects = CityMaster.objects.all()
	blood_groupObjects = BloodGroupMaster.objects.all()
	genderObjects = GenderMaster.objects.all()

	return render(request,'advocate_register.html',{'countryObjects':countryObjects,'stateObjects':stateObjects,'cityObects':cityObects,'blood_groupObjects':blood_groupObjects,'genderObjects':genderObjects})

def advo_finish(request):
	return render(request,'advocate_finish.html')

def advo_login(request):
	return render(request,'advocate_login.html')

def registration(request):
	countryObjects = CountryMaster.objects.all()
	stateObjects = StateMaster.objects.all()
	cityObects = CityMaster.objects.all()
	blood_groupObjects = BloodGroupMaster.objects.all()
	genderObjects = GenderMaster.objects.all()

	response = {}
	if request.method == 'POST':
		form = request.POST

		first_name = form['first_name']
		last_name = form['last_name']
		middle_name = form['middle_name']
		gender = GenderMaster.objects.get(name = form['gender'])
		blood_group = BloodGroupMaster.objects.get(name = form['blood_group'])
		country = CountryMaster.objects.get(name = form['country'])
		state = StateMaster.objects.get(name = form['state'])
		city = CityMaster.objects.get(name = form['city'])
		date_of_birth = form['dob']
		aaddhar_no = form['adhar_number']
		password = form['password']
		mobile_number = form['mobile_number']
		email = form['email']
		license_no = form['license_no']
		address = form['address']
		pincode = form['pincode']
		activationToken = str(randomWithNDigits(8))
		lastUserId = User.objects.latest('id').id
		crt = "CRT"+str(100000+lastUserId+1)

		user = User.objects.create_user(
			username = crt,
			first_name = first_name,
			last_name = last_name,
			email = email,
			password = password,
			)
		advocateuser =  AdvocateUser.objects.create(
			user = user,
			mobile_number = mobile_number,
			middle_name = middle_name,
			email = email,
			blood_group = blood_group,
			aadhar_no = aaddhar_no,
			activationToken = activationToken,
			)
		advocateprofile = AdvocateProfile.objects.create(
			advocateId = advocateuser,
			gender = gender,
			dob = date_of_birth,
			country = country,
			state = state,
			city = city,
			address = address,
			pincode = pincode,
			license_no = license_no,
			)
		return render(request,'advocate_finish.html',{'crt':crt,'user':user,'advocateuser':advocateuser,'advocateprofile':advocateprofile})
	else:
		return render(request,'advocate_register.html',{'countryObjects':countryObjects,'stateObjects':stateObjects,'cityObects':cityObects,'blood_groupObjects':blood_groupObjects,'genderObjects':genderObjects})

def adv_login(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username = username,password = password)
	print(user)
	if user is not None:
		if user.is_active:
			login(request,user)
			advocateuserObject = AdvocateUser.objects.get(user = user)
			return redirect('/advo_dashboard/')
		else:
			print('user is not logged in')
			messages.warning(request,"This is not activated")
			return render(request,'advocate_login.html')

	else:
		print(4)
		messages.warning(request,"Invalid Credential")
		return render(request,'advocate_login.html')

def advo_profile(request):
	countryObjects = CountryMaster.objects.all()
	stateObjects = StateMaster.objects.all()
	cityObjects = CityMaster.objects.all()
	blood_groupObjects = BloodGroupMaster.objects.all()
	genderObjects = GenderMaster.objects.all()

	user = request.user
	print(user)
	advocateuser = AdvocateUser.objects.get(user = user)
	advocateprofileObjects = AdvocateProfile.objects.get(advocateId = advocateuser)

	return render(request,'advocate_profile.html',{'user':user,'advocateuser':advocateuser,'advocateprofileObjects':advocateprofileObjects,'countryObjects':countryObjects,'stateObjects':stateObjects,'cityObjects':cityObjects,'blood_groupObjects':blood_groupObjects,'genderObjects':genderObjects})

def advo_update_profile(request):
	response = {}
	user = request.user
	countryObjects = CountryMaster.objects.get(name = form['country'])
	stateObjects = StateMaster.objects.get(name = form['state'])
	cityObects = CityMaster.objects.get(name = form['city'])
	blood_groupObjects = BloodGroupMaster.objects.all()
	genderObjects = GenderMaster.objects.all()

	advocateuserObject = AdvocateUser.objects.get(user = user)
	advocateprofileObject = AdvocateProfile.objects.get(advocateId = advocateuserObject)
	if request.method == 'POST':
		form = request.POST

		blood_groupObjects = BloodGroupMaster.objects.get(name = form['blood_group'])
		genderObjects = GenderMaster.objects.get(name = form['gender'])

		advocateuserObject.user.first_name = form['first_name']
		advocateuserObject.user.last_name = form['last_name']
		advocateuserObject.middle_name = form['middle_name']
		advocateuserObject.user.email = form['email']
		advocateuserObject.email = form['email']
		advocateuserObject.mobile_number = form['mobile_number']
		advocateprofileObject.gender = genderObjects
		advocateuserObject.blood_group = blood_groupObjects
		advocateuserObject.aaddhar_no = form['aaddhar_no']
		advocateprofileObject.country = countryObjects
		advocateprofileObject.state = stateObjects
		advocateprofileObject.city = cityObects
		advocateprofileObject.dob = form['dob']
		advocateprofileObject.address = form['address']
		advocateprofileObject.pincode = form['pincode']
		advocateprofileObject.license_no = form['license_no']
		user.save()
		advocateuserObject.save()
		advocateprofileObject.save()
		return redirect('/advo_profile/')
	else:
		return redirect('/advo_profile/')


def advo_dashboard(request):
	user = request.user
	advoUser = request.user.advocateuser
	notificationObject = AdvocateNotificationMaster.objects.filter(advocateId = advoUser)
	return render(request,'advocate_dashboard.html',{'notificationObject':notificationObject,'advoUser':advoUser})

def tracked_client(request):
	user = request.user
	advoUser = request.user.advocateuser
	notificationObject = AdvocateNotificationMaster.objects.filter(advocateId = advoUser)
	return render(request,'tracked_client.html',{'advoUser':advoUser,'notificationObject':notificationObject})


def sendmessage(request):
	response = {}
	if request.method == 'POST':
		form = request.POST

		first_name = form['name']
		email = form['email']
		subject = form['subject']
		message = form['message']

		user = User.objects.get(
			first_name = first_name,
			# last_name = last_name,
			email = email,
			)

		newMessage = SendMessage.objects.get_or_create(
			name = first_name,
			email = email,
			subject = subject,
			message = message,
			)
		return render(request,'index.html')
	else:
		return HttpResponse("your message has been sent!!")




def searchClient(request):
	user = request.user
	advocateuserObject = AdvocateUser.objects.get(user = user)
	if request.method == 'POST':
		form = request.POST

		userObject = User.objects.get(username = form['search'])
		RegistrationObject = Registration.objects.get(user = userObject)

		return render(request,'tracked_client.html',{'RegistrationObject':RegistrationObject})


	else:
		return HttpResponse(' user not found')














#function for generating activationToken
def randomWithNDigits(n):
	range_start = 10**(n-1)
	range_end = (10**n)-1
	return randint(range_start, range_end)
