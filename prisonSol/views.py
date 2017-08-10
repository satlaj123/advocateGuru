from django.shortcuts import render, redirect
from random import randint
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *


def plain(request):
	return render(request,'plain.html')

def index(request):
	return render(request,'index.html')

def form(request):
	countryObjects = CountryMaster.objects.all()
	stateObjects = StateMaster.objects.all()
	cityObects = CityMaster.objects.all()
	blood_groupObjects = BloodGroupMaster.objects.all()
	genderObjects = GenderMaster.objects.all()
	return render(request,'form.html',{'countryObjects':countryObjects,'stateObjects':stateObjects,'cityObects':cityObects,'blood_groupObjects':blood_groupObjects,'genderObjects':genderObjects})

def finish(request):
	return render(request,'finish.html')

def profile_1(request):
	return render(request,'profile_1.html')

def homepage(request):
	return render(request,'homepage.html')

def dashboard(request):
	return render(request,'dashboard.html')


def register(request):

	countryObjects = CountryMaster.objects.all()
	stateObjects = StateMaster.objects.all()
	cityObects = CityMaster.objects.all()
	blood_groupObjects = BloodGroupMaster.objects.all()
	genderObjects = GenderMaster.objects.all()


	response = {}
	if request.method =='POST':
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
		aadhar_no = form['adhar_number']
		password = form['password']
		# cpassword = form['confirm_password']
		mobile_number = form['mobile_number']
		email = form['email']
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
		newUser = Registration.objects.get_or_create(
			user = user,
			middle_name = middle_name,
			first_name = first_name,
			last_name = last_name,
			gender = gender,
			blood_group = blood_group,
			country = country,
			state = state,
			city = city,
			date_of_birth = date_of_birth,
			email = email,
			mobile_number = mobile_number,
			aadhar_no = aadhar_no,
			activationToken = activationToken,
			address = address,
			pincode = pincode,

			)
		return render(request,'finish.html',{'crt':crt,'user':user,'newUser':newUser})
	else:
		return render(request,'form.html',{'countryObjects':countryObjects,'stateObjects':stateObjects,'cityObects':cityObects,'blood_groupObjects':blood_groupObjects,'genderObjects':genderObjects})


@csrf_exempt
def signIn(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username = username, password = password)
	print(user)
	if user is not None:
		if user.is_active:
			login(request,user)
			print('user is logged in')			
			RegisterObject = Registration.objects.get(user = user)
			return redirect('/dashboard/')
		else:
			print('user is not logged in')
			messages.warning(request,"This account is not activated")
			return render(request,'login.html')

	else:
		print(4)
		messages.warning(request,"Invalid Credentials!!")
		return render(request,'login.html')

def loginpage(request):
	return render(request,'login.html')


def profile_1(request):

	countryObjects = CountryMaster.objects.all()
	stateObjects = StateMaster.objects.all()
	cityObjects = CityMaster.objects.all()
	blood_groupObjects = BloodGroupMaster.objects.all()
	genderObjects = GenderMaster.objects.all()

	user = request.user
	
	print(user)
	profileObjects = Registration.objects.get(user = user)

	return render(request,'profile_1.html',{'profileObjects':profileObjects, 'user':user,'countryObjects':countryObjects,'stateObjects':stateObjects,'cityObjects':cityObjects,'blood_groupObjects':blood_groupObjects,'genderObjects':genderObjects})

# @csrf_exempt
# @login_required(login_url = '/signIn')
def update_profile(request):
	response = {}
	user = request.user

	profileObjects = Registration.objects.get(user = user)
	
	countryObjects = CountryMaster.objects.all()
	stateObjects = StateMaster.objects.all()
	cityObjects = CityMaster.objects.all()
	if request.method == 'POST':
		form = request.POST


		genderObjects = GenderMaster.objects.get(name = form['gender'])
		blood_Objects = BloodGroupMaster.objects.get(name = form['blood_group'])
		
		user.first_name = form['first_name']
		user.last_name = form['last_name']
		profileObjects.middle_name = form['middle_name']

		user.email = form['email']
		profileObjects.email = form['email']
		profileObjects.mobile_number = form['mobile_number']
		profileObjects.gender = genderObjects
		profileObjects.blood_group = blood_Objects
		profileObjects.country = countryObjects
		profileObjects.state = stateObjects
		profileObjects.city = cityObjects
		profileObjects.date_of_birth = form['dob']
		profileObjects.address = form['address']
		profileObjects.pincode = form['pincode']
		profileObjects.aadhar_no = form['adhar_number']

		user.save()
		profileObjects.save()
		return redirect('/profile_1/')
	else:
		return redirect('/profile_1/')

def clientAppointment(request):
	user = request.user
	clientUser = Registration.objects.get(user = user)
	appointmentUser = PrisonAppointmentsMaster.objects.fileter(status = 'pending')

	return render(request,'client_appointment.html',{'clientUser':clientUser,'appointmentUser':appointmentUser})
			

def randomWithNDigits(n):
	range_start = 10**(n-1)
	range_end = (10**n)-1
	return randint(range_start, range_end)
