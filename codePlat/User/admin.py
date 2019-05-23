from django.contrib import admin

from django.contrib import admin
from . import models

admin.site.register(models.NormalUser)
admin.site.register(models.ExpertUser)
admin.site.register(models.Administrator)
admin.site.register(models.BuyResources)
admin.site.register(models.LikeResources)