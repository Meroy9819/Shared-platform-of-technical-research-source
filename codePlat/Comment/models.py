from django.db import models
from TechResource.models import SciAchi
from User.models import NormalUser
import django.utils.timezone
# Create your models here.
class Comment:
    Comment_id=models.AutoField(
        primary_key=True,
    )
    CommentResourceid=models.ForeignKey(SciAchi,on_delete=models.CASCADE)
    CommentUSerid=models.ForeignKey(NormalUser,on_delete=models.CASCADE)
    CommentTime=models.DateTimeField(auto_now_add=True)
    CommentTitle=models.CharField(max_length=100,)
    CommentContent=models.CharField(
        max_length=5000,
        null=True,
    )

    class Meta:
        verbose_name="评论"
        verbose_name_plural="评论"