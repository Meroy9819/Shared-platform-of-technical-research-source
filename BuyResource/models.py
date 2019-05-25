from django.db import models
from User.models import NormalUser
from TechResource.models import SciAchi
from django.utils import timezone
# Create your models here.

class BuyResources(models.Model):
	transaction_id=models.AutoField(
		primary_key=True,
	)
	buyer_id=models.ForeignKey(NormalUser, on_delete=models.CASCADE)
	buy_resource_id=models.ForeignKey(SciAchi,on_delete=models.CASCADE)
	time=models.DateTimeField(default = timezone.now)
	class Meta:
		verbose_name = "购买资源"
		verbose_name_plural = "购买资源"