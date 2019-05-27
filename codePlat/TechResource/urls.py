from django.conf.urls import url
from rest_framework import routers
from django.urls import path
from . import views

app_name = 'TechResource'

urlpatterns = [
    path('', views.post_list, name='post_list'), # 列表页的url规则
    path('<int:resource_id>', # 详情页的url规则
         views.post_detail,
         name='post_detail'),
]
