from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url,include
from django.views.generic import TemplateView

from . import views
urlpatterns = [
    url(r'^register/$', views.Register.as_view(), name='register'),
    url(r'^login/$',views.Login.as_view(), name="login"),
    url(r'^logout/$', views.logout, name="logout"),
]