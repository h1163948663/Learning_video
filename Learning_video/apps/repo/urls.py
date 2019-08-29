from django.conf.urls import url,include
from . import views
urlpatterns = [
    url(r'^index/$',views.index,name="index"),
    url(r'greenhand/$',views.greenhand,name="greenhand"),
    url(r'^courese/$', views.CouresList, name="CouresList"),
]
