# -*- coding: utf-8 -*-
from django.db import models
from User.models import expert
#from label.models import label
# Create your models here.
class  Resource(models.Model):
    resource_id = models.AutoField( #? 如果auto范围超过int_max怎么处理
        primary_key = True,
        )
    name = models.CharField(
        max_length = 512,
        )
    type = models.CharField(
		max_length = 20,
		null = True,
        )
    def __str__(self):  # 在Python3中用 __str__ 代替 __unicode__
         return self.name
#	ownlabels=models.ManyToManyField(
#		label,
#		blank = True,
#		)
    #


class Inst(models.Model):
    inst=models.OneToOneField(
        'resource',
        primary_key=True,
        on_delete=models.CASCADE,
    )
    estaDate=models.DateTimeField(
        default=""
    )
    haveexpert=models.ManyToManyField(expert,blank=True)
    def __str__(self):  # 在Python3中用 __str__ 代替 __unicode__
        return self.inst.name

class SciAchi(models.Model):
    sciAchi = models.OneToOneField(
        'resource',
        primary_key=True,
        on_delete=models.CASCADE,
    )
    sciAchiUrl = models.CharField(
        max_length=512,
        null=True,
    )
    abstract = models.CharField(
        max_length=1024,
        null=True,
    )
    keywordSeq = models.CharField(
        max_length=256,
        null=True,
    )
    sciAchiPrice=models.FloatField(
        default=0.0,
        null=True,
    )
    sciAchiType=models.CharField(
        max_length=50,
        null=True,
    )
    instNum=models.OneToOneField(
        'inst',
        null=True,
        on_delete=models.CASCADE,
    )
   # authorNumSeq=models.OneToManyField(expert,blank=True,on_delete=models.CASCADE,)
    refCount=models.IntegerField(
        default=0,
        null=True,
    )
    publishDate=models.DateTimeField(
        default="",
        null=True,
    )

    def __str__(self):  # 在Python3中用 __str__ 代替 __unicode__
        return self.sciAchi.name
