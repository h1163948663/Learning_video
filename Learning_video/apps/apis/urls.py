from django.conf.urls import url
from . import views
urlpatterns = [
    #生成验证码图片
    url(r'^get_captcha/$', views.get_captcha, name='get_captcha'),
    ##检查电话
    url(r'^get_mobile_captcha/$',views.get_mobile_captcha,name='get_mobile_captcha'),
    #检查验证码
    url(r'^check_captcha/$', views.check_captcha, name='check_captcha'),
    url(r'^mobile_captcha/$', views.get_mobile_captcha, name='mobile_captcha'),
    # url(r'^coureses/$',views.get_coureses,name="get_coureses"),
    url(r'^courese/$',views.CouresList.as_view(),name="CouresList"),
    url(r'^search/$',views.CoureseSearch.as_view(),name="CoureseSearch")
    # url(r'^courese/coolection/(?P<id>\d+)/$'),

]