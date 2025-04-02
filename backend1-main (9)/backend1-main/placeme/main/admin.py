from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Tutor)
admin.site.register(Student)
admin.site.register(Marks)
admin.site.register(PlacementOffer)
admin.site.register(Application)
admin.site.register(PlacementOfficer)
admin.site.register(Department)
admin.site.register(Notification)
admin.site.register(TutorApproval)
admin.site.register(PlacementApproval)

# Register your models here.
