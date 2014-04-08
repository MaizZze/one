from django.contrib import admin
from one_app import models

admin.site.register(models.Group)
admin.site.register(models.Property)
admin.site.register(models.Statistic)