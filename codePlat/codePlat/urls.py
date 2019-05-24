from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.urls import path,re_path
from . import view
from learn import views as learn_views
from User import views as user_views
from TechResource import views as Tech_views
from  django.contrib.auth import views as auth_views
urlpatterns = [
    url(r'^$',view.hello),
    path('admin/', admin.site.urls),
    path(r'index/', user_views.index),
    path(r'resource/',Tech_views.SciAchiViewSet.list_all),
    re_path(r'resource/(?P<resource_id>\d{1,2})/',Tech_views.SciAchiViewSet.list_one),


   path(r'login/', user_views.login),
    path(r'register/', user_views.register),
   path(r'logout/', user_views.logout),
    url(r'^confirm/', user_views.user_confirm),
   # url(r'captcha', include('captcha.urls'))
 #   path('resource/', include('Resource.urls')),
]
