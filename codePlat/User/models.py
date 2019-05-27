# coding=utf-8
from django.db import models
#from label.models import label
import django.utils.timezone as timezone
from django import forms
from TechResource.models import SciAchi

class NormalUser(models.Model):
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
		max_length = 1024,
		)
	#用户积分
	point = models.FloatField(
		null = True,
		)
	#用户类型
	#1 普通用户
	#2 该用户有专家主页
	#3 管理员
	type = models.IntegerField(max_length=3,default=1)
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
		default='00000000',
	)
	corresponding_expert_id=models.IntegerField(
		default=0
	)
	corrsponding_admin_id=models.IntegerField(
		default=0
	)
	has_confirmed = models.BooleanField(default=False)
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
	#专家编号
	expert_id = models.AutoField(
		primary_key=True,
	)
	#如有，对应的用户编号
	corresponding_user_id=models.IntegerField(
		default=-1
	)
	#所在机构
	institution=models.CharField(
		max_length=128,
		null=True,
	)
	#被引用数
	reference_number=models.IntegerField(
		null=True,
	)
	#论文发表数量
	paper_number=models.IntegerField(
		null=True,
	)
	#H指数
	H_index=models.IntegerField(
		null=True,
	)
	#G指数
	G_index=models.IntegerField(
		null=True,
	)
	#领域
	field=models.IntegerField(
		null=True,
	)
	class Meta:
		ordering = ["expert_id"]
		verbose_name = "专家"
		verbose_name_plural = "专家"

class Administrator(models.Model):
	#管理员编号
	admin_id=models.AutoField(
		primary_key=True,
		default=0
	)
	#管理员名字
	admin_name=models.CharField(
		max_length=30,
		default="No yet"
	)
	#管理员密码
	admin_password=models.CharField(
		max_length=100,
		default=""
	)

	class Meta:
		ordering = ["admin_id"]
		verbose_name = "管理员"
		verbose_name_plural = "管理员"


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

