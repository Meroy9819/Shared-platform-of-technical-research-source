from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.urls import path,re_path
from . import view
from learn import views as learn_views
from User import views as user_views
from TechResource import views as Tech_views
from UserComment import views as Comment_views
from  django.contrib.auth import views as auth_views
from  django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from Like import views as like_views
from Report import views as report_views
from UserComment import views as comment_views
urlpatterns = [
    url(r'^$',view.hello),
    path('admin/', admin.site.urls),
    path(r'index/', user_views.index),
    path(r'resource/',Tech_views.list_all),
    re_path(r'resource/(?P<resource_id>\d{1,2})/',Tech_views.list_one),
    re_path(r'^comment/(?P<resource_id>[0-9]+)/$',Comment_views.create_comment,name='paper_comment'),
    path(r'^comment/',Comment_views.comment_success),
    path(r'test/', TemplateView.as_view(template_name="index.html")),

    #用户主页展示
    #此处我用了redirect方法提示登录，可能连接的时候需要修改路径
    path(r'userindex/',user_views.show_user),

    #专家主页展示
    #此处需要前端往后端传数据：当前专家主页的expert_id
    url(r'^expertindex/(?P<expert_id>[0-9]+)/$',user_views.show_expert),

    #收藏某个资源
    #此处需要前端往后端传数据：当前科技资源主页的resource_id
    url(r'^like/(?P<expert_id>[0-9]+)/$',like_views.create_like),

    #举报某个资源
    #前端往后端传表单，POST；以及一个参数：当前资源的resource_id
   url(r'^report/(?P<expert_id>[0-9]+)/$', report_views.create_report),

    #评论某个资源
    #前端往后端传表单。POST；以及一个参数：当前资源的resource_id
    url(r'^comment/(?P<expert_id>[0-9]+)/$', comment_views.create_comment),


   path(r'login/', user_views.login),
    path(r'register/', user_views.register),
   path(r'logout/', user_views.logout),
    url(r'^confirm/', user_views.user_confirm),
   # url(r'captcha', include('captcha.urls'))
 #   path('resource/', include('Resource.urls')),
]
