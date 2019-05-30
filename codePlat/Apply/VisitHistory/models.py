from django.db import models
from User.models import NormalUser
from TechResource.models import SciAchi
from User.models import ExpertUser
class VisitResourceHistory(models.Model):
    SciAchi_History_id=models.AutoField(
        primary_key=True,
    )
    visit_user=models.ForeignKey(NormalUser,on_delete=models.CASCADE)
    visit_resource=models.ForeignKey(SciAchi,on_delete=models.CASCADE)
    visit_time=models.DateTimeField(auto_now_add=True)

class VisitExpertHistory(models.Model):
    Expert_History_id=models.AutoField(
        primary_key=True,
    )
    visit_user=models.ForeignKey(NormalUser,on_delete=models.CASCADE)
    visit_expert=models.ForeignKey(ExpertUser,on_delete=models.CASCADE)
    visit_time=models.DateTimeField(auto_now_add=True)
