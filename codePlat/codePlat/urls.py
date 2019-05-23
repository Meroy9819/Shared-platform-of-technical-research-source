from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.urls import path,re_path
from . import view
from learn import views as learn_views
from User import views as user_views
from TechResource import views as Tech_views
from school import views as school_views
urlpatterns = [
    url(r'^$',view.hello),
    path('admin/', admin.site.urls),
    path('add/', learn_views.add, name='add'),
    path('index1/', learn_views.index1),
    path(r'index/', user_views.NormalUserViewSet.index),
    path(r'login/', user_views.NormalUserViewSet.login),
    path(r'register/', user_views.NormalUserViewSet.register),
    path(r'logout/', user_views.NormalUserViewSet.logout),
    path(r'base/',user_views.NormalUserViewSet.base),
    path(r'title/',school_views.schools),
    re_path(r'school/(?P<id>\d{1,2})',school_views.school),
    path(r'resource/',Tech_views.SciAchiViewSet.list_all),
    re_path(r'resource/(?P<resource_id>\d{1,2})/',Tech_views.SciAchiViewSet.list_one),

   # url(r'captcha', include('captcha.urls'))
 #   path('resource/', include('Resource.urls')),
]
