from django.db import models
from User.models import NormalUser
from TechResource.models import SciAchi

# Create your models here.
class LikeResources(models.Model):
	like_id=models.AutoField(
		primary_key=True,
	)
	liker_user=models.ForeignKey(NormalUser, on_delete=models.CASCADE)
	like_resource_id = models.ForeignKey(SciAchi, on_delete=models.CASCADE)
	objects = models.Manager()

	def __str__(self):
		return self.liker_user.name + ":   " + self.like_resource_id.name

	class Meta:
		verbose_name = "收藏"
		verbose_name_plural = "收藏"