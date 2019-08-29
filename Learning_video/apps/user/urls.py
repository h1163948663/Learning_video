from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url,include
from django.views.generic import TemplateView

from . import views
urlpatterns = [
    #注册
    url(r'^register/$', views.Register.as_view(), name='register'),
    url(r'^questions/$',views.questions,name="questions"),
    # url(r'^login/$',views.Login.as_view(template_name='user/login.html'),name="login")
    # 登录  
    url(r'^login/$',views.Login.as_view(), name="login"),
    # 退出  
    url(r'^logout/$', views.logout, name="logout"),
    # url(r'^login2/$',views.login2.as_view(),name="login2")
]