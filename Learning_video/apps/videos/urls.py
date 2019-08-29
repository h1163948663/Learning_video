from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^python/$',views.PythonVideos.as_view(), name="questions"),
    url(r'^courese/$',views.Coureses.as_view(),name="courese"),
    url(r'^courese/(?P<id>\d+)/$',views.CoureseDetail.as_view(),name="courese_detail"),
    url(r'^$',views.index,name="index")

]