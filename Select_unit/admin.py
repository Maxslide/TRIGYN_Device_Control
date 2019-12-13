from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(AC)
admin.site.register(ChangeInAC)
admin.site.register(FAN)
admin.site.register(ChangeInFAN)
admin.site.register(Geyser)
admin.site.register(ChangeInGeyser)
admin.site.register(Bulb)
admin.site.register(ChangeInBulb)
admin.site.register(Smart_Wifi)
admin.site.register(ChangeInWifi)
admin.site.register(Car_Book)