from django.conf.urls import url
from learn import views
from django.urls import path
from django.contrib import admin
from . import views
app_name='learn'
urlpatterns = [
    url(r'^b', views.index1),
    url(r'^a', views.test),
]
