from django.shortcuts import render,HttpResponse
from .models import Apply,Verification
from .forms import ApplyForm,VerificationForm
from User.models import NormalUser,ExpertUser
import json

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
            new_apply=Apply()
            new_apply.apply_user=user
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


