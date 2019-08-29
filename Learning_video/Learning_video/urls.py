
from django.contrib import admin
from django.conf.urls import url,include
from . import views
from .settings import MEDIA_ROOT
from django.views.static import serve

urlpatterns = [
    url(r'^admin/',admin.site.urls),
    # url(r'^vip/',include('apps.vip.urls',namespace="vip")),
    url(r'^user/',include('apps.user.urls',namespace="user")),
    url(r'^questions/',include('apps.questions.urls',namespace='questions')),
    # url(r'^privacy/',views.test,name='privacy'),
    url(r'^paths/',include('apps.repo.urls',namespace='paths')),
    # url(r'^labs/',views.test,name='labs'),
    # url(r'^edu/',views.test,name='edu'),
    # url(r'^developer',views.test,name='developer'),
    url(r'^courses/',views.test,name='courses'),
    # url(r'^bootcamp/',views.test,name='bootcamp'),
    url(r'^index/$',views.index,name='index'),
    url(r'^apis/',include('apps.apis.urls',namespace="apis")),
    url(r'^',include('apps.videos.urls',namespace="videos")),
    url(r'^login',views.login,name="login"),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    # url(r'^videos/',include('apps.videos.urls',namespace="videos")),
    url(r'^ckeditor/',include('ckeditor_uploader.urls')),
    url(r'^repo/',include('apps.repo.urls',namespace="repo"))

]
