from django.shortcuts import render
from .models import VisitResourceHistory,VisitExpertHistory
from User.models import NormalUser,ExpertUser
from TechResource.models import SciAchi
from django.shortcuts import render,get_object_or_404,redirect,HttpResponse
import json
from django.utils import timezone
#增加资源类访问记录
def add_visit_resource_history(request,resource_id):
    if request.session.get('is_login', None):
        resource=SciAchi.objects.filter(resource_id=resource_id)
        username=request.session.get('username','')
        user = NormalUser.objects.get(username=username)
        try:
            result=VisitResourceHistory.objects.get(visit_user=user,visit_resource=resource)
            result.visit_time=timezone.now()
            result.save()
            return HttpResponse(json.dumps("访问记录更新成功"), content_type='application/json')
        except:
            new_visit=VisitResourceHistory()
            new_visit.visit_resource=resource
            new_visit.visit_user=user
            new_visit.save()
            return HttpResponse(json.dumps("访问记录存储成功"),content_type='application/json')

#增加专家类访问记录
def add_visit_expert_history(request,expert_id):
    if request.session.get('is_login', None):
        expert=ExpertUser.objects.filter(expert_id=expert_id)
        username=request.session.get('username','')
        user = NormalUser.objects.get(username=username)
        try:
            result=VisitExpertHistory.objects.get(visit_user=user,visit_expert=expert)
            result.visit_time=timezone.now()
            result.save()
            return HttpResponse(json.dumps("访问记录更新成功"), content_type='application/json')
        except:
            new_visit=VisitExpertHistory()
            new_visit.visit_resource=expert
            new_visit.visit_user=user
            new_visit.save()
            return HttpResponse(json.dumps("访问记录存储成功"),content_type='application/json')

#定期清理过期的访问记录