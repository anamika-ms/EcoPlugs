from django.contrib import admin
from . models import reg,service_reg,feed,station,service,pay,super_user

# Register your models here.

admin.site.register(reg)

admin.site.register(service_reg)

admin.site.register(feed)

admin.site.register(station)

admin.site.register(service)

admin.site.register(pay)

admin.site.register(super_user)