from django.db import models
from User.models import NormalUser
from TechResource.models import SciAchi
# Create your models here.
class report:
	report_id=models.AutoField(
		primary_key=True,
	)
	report_user=models.ForeignKey(NormalUser,on_delete=True)
	report_resource_id=models.ForeignKey(SciAchi,on_delete=True)
	report_context=models.CharField(max_length=6000,default="Nothing has been written here")
	report_time=models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.report_user.name + ":   " + self.report_resource_id.name
	class Meta:
		verbose_name = "举报信息"
		verbose_name_plural = "举报信息"
