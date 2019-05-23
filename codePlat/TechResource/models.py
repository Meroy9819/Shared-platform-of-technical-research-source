# -*- coding: utf-8 -*-
from django.db import models
from User.models import expert
#from label.models import label
# Create your models here.
class SciAchi(models.Model):
    #	ownlabels=models.ManyToManyField(
    #		label,
    #		blank = True,
    #		)
    #
    # 资源编号
    resource_id = models.AutoField(  # ? 如果auto范围超过int_max怎么处理
        primary_key=True,
    )
    # 资源名称
    name = models.CharField(
        max_length=512,
        default="No name yet"
    )
    #论文链接
    sciAchiUrl = models.CharField(
        max_length=512,
        null=True,
    )
    #摘要
    abstract = models.CharField(
        max_length=1024,
        null=True,
    )
    #关键词序列
    keywordSeq = models.CharField(
        max_length=256,
        null=True,
    )
    #价格
    sciAchiPrice=models.FloatField(
        default=0.0,
        null=True,
    )
   # authorNumSeq=models.OneToManyField(expert,blank=True,on_delete=models.CASCADE,)
    #引用数
    refCount=models.IntegerField(
        default=0,
        null=True,
    )
    #发表年份
    publishYear=models.IntegerField(
        null=True,
    )

    class Meta:
        verbose_name="科技成果"
        verbose_name_plural="科技成果"