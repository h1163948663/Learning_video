from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^get_captcha/$', views.get_captcha, name='get_captcha'),
    url(r'^get_mobile_captcha/$',views.get_mobile_captcha,name='get_mobile_captcha'),
    url(r'^check_captcha/$', views.check_captcha, name='check_captcha'),
    url(r'^mobile_captcha/$', views.get_mobile_captcha, name='mobile_captcha'),
    url(r'^courese/$',views.CouresList.as_view(),name="CouresList"),
    url(r'^search/$',views.CoureseSearch.as_view(),name="CoureseSearch"),
    url(r'^collect/',views.collect,name='collect'),
]