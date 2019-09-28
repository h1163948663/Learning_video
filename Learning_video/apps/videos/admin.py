from django.contrib import admin

# Register your models here.
from . import models
admin.site.register(models.Courese)
# admin.site.register(models.PythonCoures)
admin.site.register(models.ALLCoureslist)
admin.site.register(models.Category)