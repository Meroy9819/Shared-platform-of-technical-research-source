from django.db import models
from User.models import NormalUser
from TechResource.models import SciAchi
from User.models import ExpertUser
from UserComment.models import Comment
# 举报资源
class report(models.Model):
	error = (
		('title', '标题错误'),
		('author', '作者错误'),
		('keyword', '关键词错误'),
		('year', '发表年份错误'),
		('abstract', '摘要错误'),
		('author', '作者错误'),
		('sciAchiUrl','论文文件错误')
	)
	report_id=models.AutoField(
		primary_key=True,
	)
	report_user=models.ForeignKey(NormalUser,on_delete=True)
	report_resource_id=models.ForeignKey(SciAchi,on_delete=True)
	report_context=models.CharField(max_length=6000,default="Nothing has been written here")
	report_time=models.DateTimeField(auto_now_add=True)
	report_error=models.CharField(
		max_length=32, choices=error, default='标题错误'
	)
	#举报信息的状态
	#1：提交成功，正在审核
	#2：审核通过，已处理
	#3：审核未通过，已驳回
	report_status=models.IntegerField(default=1)
	def __str__(self):
		return self.report_user.name + ":   " + self.report_resource_id.name
	class Meta:
		verbose_name = "举报成果信息"
		verbose_name_plural = "举报成果信息"

#举报专家信息
class report_expert(models.Model):
	error = (
		('name', '姓名错误'),
		('institution', '所在机构错误'),
		('paper_number', '论文发表数量错误'),
		('H_index', 'H指数'),
		('G_index', 'G指数'),
		('field', '领域错误'),
	)
	reportexpert_id=models.AutoField(
		primary_key=True,
	)
	report_user=models.ForeignKey(NormalUser,on_delete=True)
	report_expert_id=models.ForeignKey(ExpertUser,on_delete=True)
	report_context=models.CharField(max_length=6000,default="Nothing has been written here")
	report_time=models.DateTimeField(auto_now_add=True)
	report_error=models.CharField(
		max_length=32, choices=error, default='标题错误'
	)
	#举报信息的状态
	#1：提交成功，正在审核
	#2：审核通过，已处理
	#3：审核未通过，已驳回
	report_status=models.IntegerField(default=1)

	def __str__(self):
		return self.report_user.name + ":   " + self.report_expert_id.name
	class Meta:
		verbose_name = "举报专家信息"
		verbose_name_plural = "举报专家信息"


#举报评论信息
class report_comment(models.Model):
	reportcomment_id=models.AutoField(
		primary_key=True,
	)
	report_user=models.ForeignKey(NormalUser,on_delete=True)
	report_comment_id=models.ForeignKey(Comment,on_delete=True)
	report_context=models.CharField(max_length=6000,default="Nothing has been written here")
	report_time=models.DateTimeField(auto_now_add=True)
	#举报信息的状态
	#1：提交成功，正在审核
	#2：审核通过，已处理
	#3：审核未通过，已驳回
	report_status=models.IntegerField(default=1)

	def __str__(self):
		return self.report_user.name
	class Meta:
		verbose_name = "举报评论"
		verbose_name_plural = "举报评论"