from django.shortcuts import render,HttpResponse
from .models import Apply,Verification
from .forms import ApplyForm,VerificationForm
from User.models import NormalUser,ExpertUser
import json
from django.forms.models import model_to_dict

#创建新的成为专家申请
def apply_to_expert(request):
    if not request.session.get('is_login', None)!=True:
        return HttpResponse(json.dumps("请先登录"),content_type='application/json')
    if request.method == "POST":
        apply_form = ApplyForm(request.POST)
        message = "请检查填写的内容！"
        if apply_form.is_valid():  # 获取数据
            apply_name =ApplyForm.cleaned_data['apply_name']
            apply_institution = ApplyForm.cleaned_data['apply_institution']
            apply_resource = ApplyForm.cleaned_data['apply_resource']
            apply_resourceyear = ApplyForm.cleaned_data['apply_resourceyear']
            apply_field = ApplyForm.cleaned_data['apply_field']
            apply_photo = ApplyForm.cleaned_data['apply_photo']
            username=request.session.get('username','')
            user=NormalUser.objects.filter(username=username)
            if user.user_type==2:
                return HttpResponse(json.dumps("您已经是专家了"),content_type='application/json')
            if user.user_type==3:
                return HttpResponse(json.dumps("喂你是管理员呀！"),content_type='application/json')
            new_apply=Apply()
            new_apply.apply_user=user
            new_apply.apply_name=apply_name
            new_apply.apply_institution =apply_institution
            new_apply.apply_resource = apply_resource
            new_apply.apply_resourceyear = apply_resourceyear
            new_apply.apply_field  = apply_field
            new_apply.apply_photo  = apply_photo
            new_apply.save()
            return HttpResponse(json.dumps('提交申请成功'),content_type='application/json')
        apply_form = ApplyForm
        return HttpResponse(json.dumps('哈哈哈哈哈'),content_type='application/json')

#创建专家认领申请
def verification_to_expert(request,expert_id):
    username=request.session.get('username','')
    user=NormalUser.objects.filter(usernmae=username)
    expert=ExpertUser.objects.filter(expert_id=expert_id)
    if not request.session.get('is_login', None):
        return HttpResponse(json.dumps('请先登录'),content_type='application/json')
    if request.method == "POST":
        veri_form = VerificationForm(request.POST)
        message = "请检查填写的内容！"
        if veri_form.is_valid():
            verification_image = veri_form.cleaned_data['verification_image']
            new_veri=Verification
            new_veri.verification_expert=expert
            new_veri.verification_user=user
            new_veri.verification_image=verification_image
            new_veri.save()
            return HttpResponse(json.dumps('提交认领申请成功'),content_type='application/json')
    veri_form = VerificationForm
    return render(request, 'login/login.html', locals())


#列出所有的未处理的创建成为专家的申请
def not_done_applytoexpert(request):
    ret={}
    json_list=[]
    result=Apply.objects.filter(apply_status=1)
    for item in result:
        json_dict=model_to_dict(item)
        json_list.append(json_dict)
    return HttpResponse(json.dumps(ret),content_type='application/json')


#列出所有的已处理的创建成为专家的申请
def not_done_applytoexpert(request):
    ret={}
    json_list=[]
    result=Apply.objects.filter(apply_status=2)
    for item in result:
        json_dict=model_to_dict(item)
        json_list.append(json_dict)
    return HttpResponse(json.dumps(ret),content_type='application/json')
