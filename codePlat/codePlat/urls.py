from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from . import view
from learn import views as learn_views
from User import views as user_views
urlpatterns = [
    url(r'^$',view.hello),
    path('admin/', admin.site.urls),
    path('add/', learn_views.add, name='add'),
    path(r'index/', user_views.NormalUserViewSet.index),
    path(r'login/', user_views.NormalUserViewSet.login),
    path(r'register/', user_views.NormalUserViewSet.register),
    path(r'logout/', user_views.NormalUserViewSet.logout),
    path(r'base/',user_views.NormalUserViewSet.base),
    url(r'captcha', include('captcha.urls'))
 #   path('resource/', include('Resource.urls')),
]
