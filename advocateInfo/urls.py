from django.conf.urls import url, include, patterns
from advocateInfo.views import *
urlpatterns = [
	url(r'^advo_register_show/',advo_register_show,name = 'advocate registration form'),
	url(r'^registration/', registration, name = 'registration page'),
	url(r'^advo_finish/',advo_finish, name = 'finish page'),
	url(r'^advo_login/',advo_login,name = 'login for advocate'),
	url(r'^advo_profile/',advo_profile, name = 'profile for advocate'),
	url(r'^adv_login/',adv_login, name = 'profile for advocate'),
	url(r'^advo_dashboard/',advo_dashboard,name = 'advocate dashboard page'),
	url(r'^searchClient',searchClient,name = 'advocate search our client'),
	url(r'^sendmessage/',sendmessage, name='sendmessage page'),
	url(r'^tracked_client',tracked_client,name ='tracked the client'),
]