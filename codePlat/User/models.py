# coding=utf-8
from django.db import models
#import TechResource.models as Tech
#from label.models import label
import django.utils.timezone as timezone
from django import forms
from TechResource.models import SciAchi


class NormalUser(models.Model):
	gender = (
		('male', '男'),
		('female', '女'),
	)
	kind=(
		('专家用户','专家用户'),
		('普通用户','普通用户'),
		('管理员','管理员'),
	)
	#用户编号
	user_id = models.AutoField(
		primary_key = True,
		)
	#用户姓名
	name = models.CharField(
		max_length = 64,
		unique = True,
		)
	#用户密码
	passwd = models.CharField(
		max_length = 32,
		)
	#用户积分
	point = models.FloatField(
		null = True,
		)
	#用户类型
	type = models.CharField(
		max_length = 32,
		choices=kind,
		default='普通用户',
		)
	#用户头像
	image = models.ImageField(
		null = True,
		)
	#用户简介
	introduction = models.CharField(
		max_length = 100, 
		null = True,
		)
	#用户邮箱
	email=models.CharField(
		max_length=100,
		null=True,
	)
	#用户性别
	sex=models.CharField(
		max_length=32, choices=gender, default='女'
	)
	c_time = models.DateTimeField(auto_now_add=True)
	#用户手机号
	phonenumber=models.CharField(
		max_length=11,
		default="00000000000",
	)
	def __str__(self):
		return self.name

	class Meta:
		ordering = ['c_time']
		verbose_name = '用户'
		verbose_name_plural = '用户'

#	buyresources = models.ManyToManyField(Tech.Resource,
#		through='model_buyresources',
#		blank=True,
#		)

class ExpertUser(models.Model):
	expert_id = models.AutoField(
		primary_key=True,
	)
	#联系电话
	contact = models.CharField(
		max_length = 128,
		null = True,
		)
	institution=models.CharField(
		max_length=128,
		null=True,
	)
	reference_number=models.IntegerField(
		null=True,
	)
	paper_number=models.IntegerField(
		null=True,
	)
	H_index=models.IntegerField(
		null=True,
	)
	G_index=models.IntegerField(
		null=True,
	)
	field=models.IntegerField(
		null=True,
	)
#	ownlabels=models.ManyToManyField(
#		label,
#		blank=True,
#		)
#	from TechResource.models import Resource
#	ownresources=models.ManyToManyField(Resource,blank=True)

class Administrator(models.Model):
	administrator = models.OneToOneField(
		'NormalUser',
		on_delete = models.CASCADE,
		default = "",
		)

class BuyResources(models.Model):
	transaction_id=models.AutoField(
		primary_key=True,
	)
	buyer_id=models.ForeignKey(NormalUser, on_delete=models.CASCADE)
	buy_resource_id=models.ForeignKey(SciAchi,on_delete=models.CASCADE)
	time=models.DateTimeField(default = timezone.now)

class LikeResources(models.Model):
	like_id=models.AutoField(
		primary_key=True,
	)
	liker_user=models.ForeignKey(NormalUser, on_delete=models.CASCADE)
	like_resource_id = models.ForeignKey(SciAchi, on_delete=models.CASCADE)

class ConfirmString(models.Model):
    code = models.CharField(max_length=256)
    user = models.OneToOneField('NormalUser',on_delete=models.CASCADE)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name + ":   " + self.code

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "确认码"
        verbose_name_plural = "确认码"