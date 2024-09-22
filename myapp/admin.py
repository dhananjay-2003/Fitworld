from django.contrib import admin
from .models import Contact
from .models import Appointment
from .models import Batch_Appointment
from .models import Feedback


admin.site.site_header = 'Fitworld'
admin.site.site_title = 'Title'
admin.site.index_title = 'Dashboard'

# Register your models here.
admin.site.register(Contact)
admin.site.register(Appointment)
admin.site.register(Batch_Appointment)
admin.site.register(Feedback)




