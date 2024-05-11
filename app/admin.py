from django.contrib import admin

from .models import Sponsor,SponsorStudent,Student,University,BaseModel
# Register your models here.

admin.site.register(Sponsor)
admin.site.register(Student)
admin.site.register(University)
admin.site.register(SponsorStudent)