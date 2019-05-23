from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.shortcuts import render, redirect
from . import models
from User.models import normal_user, expert, administrator
from User.forms import UserForm
#from institutions.models import Institution
#from label.models import label
from TechResource.models import SciAchi
from User.serializers import NormalUserSerializer, ExpertSerializer, AdministratorSerializer
#from institutions.serializers import InstitutionSerializer
#from institutions.serializers import InstitutionSerializer
from django.shortcuts import render, redirect
from . import models
from .forms import UserForm, RegisterForm
import hashlib
class NormalUserViewSet(viewsets.ModelViewSet):
    queryset = normal_user.objects.all()
    serializer_class = NormalUserSerializer

    def hash_code(s, salt='codeplat_login'):
        h = hashlib.sha256()
        s += salt
        h.update(s.encode())  # update方法只接收bytes类型
        return h.hexdigest()

    def index(request):
        pass
        return render(request, 'login/index.html')

    def login(request):
        if request.session.get('is_login', None):
            return redirect("/index/")
        if request.method == "POST":
            login_form = UserForm(request.POST)
            message = "请检查填写的内容！"
            if login_form.is_valid():
                username = login_form.cleaned_data['username']
                password = login_form.cleaned_data['password']
                try:
                    user = models.User.objects.get(name=username)
                    if user.password == hash_code(password):  # 哈希值和数据库内的值进行比对
                        request.session['is_login'] = True
                        request.session['user_id'] = user.id
                        request.session['user_name'] = user.name
                        return redirect('/index/')
                    else:
                        message = "密码不正确！"
                except:
                    message = "用户不存在！"
            return render(request, 'login/login.html', locals())

        login_form = UserForm()
        return render(request, 'login/login.html', locals())

    def register(request):
        if request.session.get('is_login', None):
            # 登录状态不允许注册。你可以修改这条原则！
            return redirect("/index/")
        if request.method == "POST":
            register_form = RegisterForm(request.POST)
            message = "请检查填写的内容！"
            if register_form.is_valid():  # 获取数据
                username = register_form.cleaned_data['username']
                password1 = register_form.cleaned_data['password1']
                password2 = register_form.cleaned_data['password2']
                email = register_form.cleaned_data['email']
                sex = register_form.cleaned_data['sex']
                if password1 != password2:  # 判断两次密码是否相同
                    message = "两次输入的密码不同！"
                    return render(request, 'login/register.html', locals())
                else:
                    same_name_user = models.User.objects.filter(name=username)
                    if same_name_user:  # 用户名唯一
                        message = '用户已经存在，请重新选择用户名！'
                        return render(request, 'login/register.html', locals())
                    same_email_user = models.User.objects.filter(email=email)
                    if same_email_user:  # 邮箱地址唯一
                        message = '该邮箱地址已被注册，请使用别的邮箱！'
                        return render(request, 'login/register.html', locals())

                    # 当一切都OK的情况下，创建新用户

                    new_user = models.User.objects.create()
                    new_user.name = username
                    new_user.password = hash_code(password1)  # 使用加密密码
                    new_user.email = email
                    new_user.sex = sex
                    new_user.save()
                    return redirect('/login/')  # 自动跳转到登录页面
        register_form = RegisterForm()
        return render(request, 'login/register.html', locals())

    def logout(request):
        if not request.session.get('is_login', None):
            return redirect('/index/')
        request.session.flush()

        return redirect('/index/')



    def base(request):
        pass
        return render(request,'login/base.html')

    @action(methods = ["POST"], detail = False)
    def Search(self, request):
        user = normal_user.objects.get(name = request.data.get("name"))
        '''
        normal_user_serializer = NormalUserSerializer(user)
        resource_serializer = ResourceSerializer(user.expert.ownresources.all(), many = True)
        institution_serializer = InstitutionSerializer(user.expert.institution_set.all(), many = True)
        
        result = []
        result.append(normal_user_serializer.data)
        result += resource_serializer.data
        result += institution_serializer.data
        '''
        return Response(user.user_id, status=status.HTTP_200_OK) 

    def list(self, request):
        serializer = NormalUserSerializer(self.GetQueryset(request), many = True)
        result = serializer.data
        for u in result:
            u.pop("passwd")
        return Response(result)

    def GetQueryset(self, request):
        name = request.query_params.get('name', None)
        pk = request.query_params.get('pk', None)
        if name is not None: 
            queryset = normal_user.objects.filter(name__contains = name)
        elif pk is not None:
            queryset = normal_user.objects.filter(user_id = pk)
        else:
            queryset = normal_user.objects.all()
        return queryset



    @action(methods = ['POST'], detail = False)
    def Login(self, request):
        username = request.POST.get("name")
        #username = "123"
        passwd = request.POST.get("passwd")
        '''
        queryset = normal_user.objects.get(name = username)
        '''
        try:
            queryset = normal_user.objects.get(name = username)
        except:
            return Response("user doest exist", status = status.HTTP_406_NOT_ACCEPTABLE)
        if queryset.passwd == passwd:
            #request.session['user_id'] = queryset.user_id
            serializer = NormalUserSerializer(queryset, many = True)
            #request.session.set_expiry(0)
            return Response(queryset.user_id, status = status.HTTP_200_OK)
        else:
            return Response('passwd is wrong', status = status.HTTP_406_NOT_ACCEPTABLE)

    @action(methods = ['GET'], detail = False)
    def Logout(self, request):
        #try:
        #    request.session.delete("session_key");
        #except KeyError:
        #    pass

        return Response("You've logged out!", status=status.HTTP_200_OK)

    @action(methods = ['POST'], detail = False)
    def user_update(self,request):
        user_pk = request.data.get('pk', None)
        
        queryset = normal_user.objects.filter( user_id = user_pk )
        if queryset.exists():
            image = request.POST.get('image')
            introduction = request.POST.get('introduction')
            thisUser = normal_user(user_id = user_pk, image = image, introduction = introduction)
            thisUser.save()
            serializer = NormalUserSerializer(queryset, many = True)
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response('user_id is wrong', status = status.HTTP_406_NOT_ACCEPTABLE) 

    @action(methods = ['GET'], detail = False)
    def Access(self,request):
        user_name = request.query_params.get('user_name', None)
        resource_name = request.query_params.get('resource_name', None)
        user=normal_user.objects.get(name=user_name)
        buyresources_set=user.buyresources.all()
        expert=user.expert
        ownresources_set=expert.ownresources.all()
        myresource=Resource.objects.get(name=resource_name)
        if myresource in buyresources_set or myresource in ownresources_set:
            return Response('True',status = status.HTTP_200_OK)
        return Response('False',status = status.HTTP_400_BAD_REQUEST)

'''    @action(methods = ['GET'], detail = False)
    def Trade(self,request):
        user_name = request.query_params.get('user_name', None)
        user=normal_user.objects.get(name=user_name)
        userid = user.user_id
        TradeRecord = user.buyresources.all()
        serializers=ResourceSerializer(TradeRecord, many = True)
        temp = serializers.data
        for tm in temp:
            m1 = model_buyresources.objects.get(normal_user_id=userid,
                resource_id = tm['resource_id'])
            tm['time']=m1.time

        return Response(temp,status = status.HTTP_200_OK)


    @action(methods = ['POST'], detail = False)
    def Buy(self,request):
        user_id = request.POST.get('user_id', None)
        resource_id = request.data.get('resource_id', None)
        myresource=Resourceesource.objects.get(resource_id=resource_id)
        mypaper=myresource.paper
        value=mypaper.value
        user=normal_user.objects.get(user_id=user_id)
        buy1=model_buyresources(normal_user=user,resource=myresource)
        return Response(status = status.HTTP_200_OK)
'''
class ExpertViewSet(viewsets.ModelViewSet):
    queryset = expert.objects.all()
    serializer_class = ExpertSerializer
    
    def list(self,request):
        user_name = request.query_params.get('name', None)
        try:
            queryset_normaluser = normal_user.objects.filter(name__regex = r'(\S* +%s +\S*)|(\S* +%s$)|(%s +\S*)|(^%s$)'%(user_name,user_name,user_name,user_name))
        except:
            return Response("user is not exists", status = status.HTTP_400_BAD_REQUEST)
        else:
            '''
            expertid = queryset_normaluser.user_id
            try:
                queryset_expert = expert.objects.get(expert_id = expertid)
            except:
                return Response("user does not exists", status = status.HTTP_400_BAD_REQUEST)
            else:
                serializer_normal = NormalUserSerializer(queryset_normaluser)
                serializer_expert = ExpertSerializer(queryset_expert )
                result = dict(serializer_normal.data,**serializer_expert.data)
                result.pop("passwd")
                result.pop("expert")
                return Response(result, status = status.HTTP_200_OK)
            '''
            normal_user_serializer = NormalUserSerializer(queryset_normaluser, many=True)
            
            expert_list = []
            for expert_ in queryset_normaluser: 
                expert_serializer = ExpertSerializer(expert_)
                expert_list += expert_serializer.data
            result = []
            result += normal_user_serializer.data
            result += expert_list
            
            return Response(result, status=status.HTTP_200_OK)
    
    def create(self, request):
        normal_user_serializer = NormalUserSerializer(data = request.data)
        expert_serializer = ExpertSerializer(data = request.data)
        if normal_user_serializer.is_valid():
            if expert_serializer.is_valid():
                thisUser = normal_user(
                    name = request.data.get("name"), 
                    passwd = request.data.get("passwd"), 
                    point = request.data.get("point"),
                    image = request.data.get("file_data"),
                    type = "expert",
                    introduction = request.data.get("introduction")
                    )
                thisUser.save()
                expert(
                    expert = thisUser,
                    contact = request.data.get("contact")
                    ).save()
                return Response(thisUser.user_id, status = status.HTTP_201_CREATED)
            return Response(normal_user.objects.get(name = request.data.get("name")).user_id, status = status.HTTP_400_BAD_REQUEST)
        return Response(normal_user.objects.get(name = request.data.get("name")).user_id, status = status.HTTP_400_BAD_REQUEST)

    @action(methods = ['GET'], detail = False)
    def Access(self,request):
        user_name = request.query_params.get('user_name', None)
        resource_name = request.query_params.get('resource_name', None)
        user=normal_user.objects.get(name=user_name)
        expert=user.expert
        resources_set=expert.ownresources.all()
        resource=Resource.objects.get(name=resource_name)
        if resource in resources_set:
            return Response('True',status = status.HTTP_200_OK)
        return Response('False',status = status.HTTP_status.HTTP_400_BAD_REQUEST)

    @action(methods = ['GET'], detail = False)
    def Relation(self,request):
        try:
            name = request.query_params.get('name', None)
            co_workers = []
            my_expert= normal_user.objects.get(name = name).expert
            queryset_resource = my_expert.ownresources.all()
            for my_resource in queryset_resource:
                co_set = my_resource.expert_set.all()
                for co_worker in co_set:
                    co_name = co_worker.expert.name
                    if co_name not in co_workers and co_name != name:
                        co_workers.append(co_name)
        except:
            pass
        return Response(co_workers,status = status.HTTP_200_OK)

    def CreateByApplysheet(applysheet):
        try:
            thisUser = normal_user.objects.get(user_id = applysheet.user.user_id)
            expert(
                expert = thisUser,
                contact = applysheet.contact,
            ).save()
            thisUser.type = "expert"
            thisUser.save()
        except Exception as e:
            raise
        return Response(status = status.HTTP_201_CREATED)
    
    @action(methods = ['POST'], detail = False)
    def AddResource(self, request):
        user_id = request.data.get("user_id")
        resource_id = request.data.get("resource_id")

        normalUser = normal_user.objects.get(user_id = user_id)
        normalUser.expert.ownresources.add(SciAchi.objects.get(resource_id = resource_id))

        return Response(status=status.HTTP_200_OK)

    @action(methods = ['POST'], detail = False)
    def Detail(self,request):
        myid = request.query_params.get('expert_id', None)
        try:
            queryset_normaluser = normal_user.objects.get(user_id = myid)
        except:
            return Response("user is not exists", status = status.HTTP_400_BAD_REQUEST)
        else:
            expertid = queryset_normaluser.user_id
            try:
                queryset_expert = expert.objects.get(expert_id = expertid)
            except:
                return Response("user does not exists", status = status.HTTP_400_BAD_REQUEST)
            else:
                serializer_normal = NormalUserSerializer(queryset_normaluser)
                serializer_expert = ExpertSerializer(queryset_expert )
                result = dict(serializer_normal.data,**serializer_expert.data)
                result.pop("passwd")
                result.pop("expert")
                return Response(result, status = status.HTTP_200_OK)
'''
    @action(methods = ['POST'], detail = False)
    def AddLabel(self, request):
        user_id = request.data.get("user_id")
        label_id = request.data.get("label_id")

        normalUser = normal_user.objects.get(user_id = user_id)
        normalUser.expert.ownlabels.add(label.objects.get(label_id = label_id))

        return Response(status=status.HTTP_200_OK)

    @action(methods = ['POST'], detail = False)
    def AddInstitution(self, request):
        user_id = request.data.get("user_id")
        institution_id = request.data.get("institution_id")

        normalUser = normal_user.objects.get(user_id = user_id)
        Institution.objects.get(institution_id = institution_id).ownexperts.add(normal_user.objects.get(user_id = user_id).expert)

        return Response(status=status.HTTP_200_OK)
'''
class AdministratorViewSet(viewsets.ModelViewSet):
    queryset = administrator.objects.all()
    serializer_class = AdministratorSerializer
    
    def create(self, request):
        normal_user_serializer = NormalUserSerializer(data = request.data)
        administrator_serializer = AdministratorSerializer(data = request.data)
        if normal_user_serializer.is_valid():
            if administrator_serializer.is_valid():
                thisNormal_user = normal_user(
                    name = request.data.get("name"), 
                    passwd = request.data.get("passwd"), 
                    point = request.data.get("point"),
                    image = request.data.get("image"),
                    type = "administrator",
                    introduction = request.data.get("introduction")
                    )
                thisNormal_user.save()
                administrator(
                    administrator = thisNormal_user
                    ).save()
                return Response(administrator_serializer.data, status = status.HTTP_201_CREATED)
            return Response(administrator_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        return Response(normal_user_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
