from django.conf.urls import url
from . import views
urlpatterns = [

    url(r'^choose_video/$',views.choose_video,name="choose_video"),
    url(r'^courese/(?P<id>\d+)/$',views.CoureseDetail.as_view(),name="courese_detail"),
    url(r'^$',views.index,name="index")
    ]