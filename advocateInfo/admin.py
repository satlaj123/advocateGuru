from django.contrib import admin
from advocateInfo.models import *

# Register your models here.
admin.site.register(AdvocateUser)
admin.site.register(AdvocateProfile)
admin.site.register(AdvocateNotificationMaster)
admin.site.register(AdvocateNotificationMaster_saver)
admin.site.register(ScheduleMaster)
admin.site.register(AdvocateAppointmentsMaster)
admin.site.register(SendMessage)
# admin.site.register(advocateUser)