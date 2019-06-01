from django.db import models
from User.models import NormalUser,ExpertUser
class Apply(models.Model):
    apply_id=models.AutoField(
        primary_key=True,
    )
    apply_user=models.ForeignKey(NormalUser,on_delete=models.CASCADE)
    apply_name=models.CharField(max_length=512)
    apply_institution=models.CharField(max_length=1024)
    apply_resource=models.CharField(max_length=1024)
    apply_resourceyear=models.CharField(max_length=8)
    apply_field=models.CharField(max_length=256)
    apply_photo=models.ImageField()
    #1:未处理
    #2：已处理，通过
    #3：处理，不通过
    apply_status=models.IntegerField(default=1)
    def __str__(self):
        return self.apply_user.username
    class Meta:
        verbose_name = "申请成为专家信息"
        verbose_name_plural = "申请成为专家信息"


class Verification(models.Model):
    verification_id=models.AutoField(
        primary_key=True,
    )
    verification_expert=models.ForeignKey(ExpertUser,on_delete=True)
    verification_user=models.ForeignKey(NormalUser,on_delete=True)
    verification_image=models.ImageField()
    def __str__(self):
        return self.verification_user.username + ":   " + self.verification_expert.name
    class Meta:
        verbose_name = "认领专家信息"
        verbose_name_plural = "认领专家信息"



