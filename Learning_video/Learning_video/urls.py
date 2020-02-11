from . import settings
from django.contrib import admin
from django.conf.urls import url,include
from django.conf.urls.static import static
from . import views
from .settings import MEDIA_ROOT,STATIC_ROOT
from django.views.static import serve
from django.views import static

urlpatterns = [
    url(r'^admin/',admin.site.urls),
    url(r'^user/',include('apps.user.urls',namespace="user")),
    url(r'^paths/',include('apps.repo.urls',namespace='paths')),
    url(r'^index/$',views.index,name='index'),
    url(r'^apis/',include('apps.apis.urls',namespace="apis")),
    url(r'^',include('apps.videos.urls',namespace="videos")),
    url(r'^login',views.login,name="login"),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url(r'^ckeditor/',include('ckeditor_uploader.urls')),
    url(r'^comment/',include('apps.comment.url',namespace="comment")),
    url('^static/(?P<path>.*)$', static.serve, {'document_root': STATIC_ROOT}, name='static'),
]

# handler403 = views.page_permission_denied
handler404 = views.page_not_found
# handler500 = views.page_inter_error