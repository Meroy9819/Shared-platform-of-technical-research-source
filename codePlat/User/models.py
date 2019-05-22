# coding=utf-8
from django.db import models
#import TechResource.models as Tech
#from label.models import label
import django.utils.timezone as timezone
from django import forms

class normal_user(models.Model):
	gender = (
		('male', '男'),
		('female', '女'),
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
		max_length = 16,
		null = True,
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

class expert(models.Model):
	expert = models.OneToOneField(
		'normal_user', 
		on_delete = models.CASCADE,
		default = "",
		)
	contact = models.CharField(
		max_length = 128,
		null = True,
		)
#	ownlabels=models.ManyToManyField(
#		label,
#		blank=True,
#		)
#	from TechResource.models import Resource
#	ownresources=models.ManyToManyField(Resource,blank=True)

class administrator(models.Model):
	administrator = models.OneToOneField(
		'normal_user',
		on_delete = models.CASCADE,
		default = "",
		)

class model_buyresources(models.Model):
	normal_user=models.ForeignKey(normal_user, on_delete=models.CASCADE)
#	resource=models.ForeignKey(Tech.Resource, on_delete=models.CASCADE)
	time=models.DateTimeField(default = timezone.now)
		
