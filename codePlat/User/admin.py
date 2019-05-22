from django.contrib import admin

from django.contrib import admin
from . import models

admin.site.register(models.normal_user)
admin.site.register(models.expert)
admin.site.register(models.administrator)