from django.db import models
from User.models import NormalUser
from TechResource.models import SciAchi
from User.models import ExpertUser

# Create your models here.
class LikeResources(models.Model):
	like_id=models.AutoField(
		primary_key=True,
	)
	liker_user=models.ForeignKey(NormalUser, on_delete=models.CASCADE)
	like_resource_id = models.ForeignKey(SciAchi, on_delete=models.CASCADE)
	objects = models.Manager()

	def __str__(self):
		return self.liker_user.username + ":   " + self.like_resource_id.name

	class Meta:
		verbose_name = "收藏成果"
		verbose_name_plural = "收藏成果"

class LikeExpert(models.Model):
	like_id=models.AutoField(
		primary_key=True,
	)
	liker_user=models.ForeignKey(NormalUser, on_delete=models.CASCADE)
	like_expert_id = models.ForeignKey(ExpertUser, on_delete=models.CASCADE)
	objects = models.Manager()

	def __str__(self):
		return self.liker_user.name + ":   " + self.like_resource_id.name

	class Meta:
		verbose_name = "收藏专家"
		verbose_name_plural = "收藏专家"