from django.contrib import admin
from . import models


# admin.site.register(models.EBSchedule)
# admin.site.register(models.TABSchedule)
# admin.site.register(models.CBSchedule)
admin.site.register(models.PMBL03Schedule)
admin.site.register(models.PMBL04Schedule)