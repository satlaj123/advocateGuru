from django.conf.urls import url, include, patterns
from prisonSol.views import *
# from django.conf import settings
urlpatterns = [
	# url(r'^registerShow',registerShow, name='registration page'),
	url(r'^register',register, name='register page'),
	url(r'^index',index, name='index page'),
	url(r'^plain/',plain, name='plain page'),
	url(r'^signIn/',signIn, name='login page'),
	url(r'^loginpage/',loginpage, name='login page'),
	# url(r'^profile/',profile, name='profile page'),
	url(r'^form/',form, name='form page'),
	url(r'^finish/',finish, name='after registration page'),
	url(r'^update_profile/',update_profile, name='update_profile page'),
	url(r'^profile_1/',profile_1, name = 'profile page'),
	url(r'^homepage', homepage, name = 'upload your file'),
	url(r'^dashboard', dashboard, name = 'dashboard your file'),
	url(r'^clientappointment',clientAppointment, name = 'clientAppointment page'),
	]