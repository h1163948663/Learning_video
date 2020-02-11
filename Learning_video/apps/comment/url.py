from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^submit_comment/(?P<id>\d+)$',views.submit_comment, name='submit_comment'),
    url(r'^get_comments/$', views.get_comments, name='get_comments'),
]