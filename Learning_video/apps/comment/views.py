from datetime import datetime

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import *
from django.template.loader import render_to_string
from apps.comment.models import Comment
from django.views.decorators.http import require_http_methods
from apps.videos.forms import CommentForm
from apps.videos.models import ALLCoureslist
from django.views.decorators.csrf import csrf_exempt

def ajax_required(f):
    """Not a mixin, but a nice decorator to validate than a request is AJAX"""
    def wrap(request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponseBadRequest()
        return f(request, *args, **kwargs)
    wrap.__doc__ = f.__doc__
    wrap.__name__ = f.__name__
    return wrap

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def submit_comment(request,id):
    video = get_object_or_404(ALLCoureslist, id=id)
    form = CommentForm(data=request.POST)


    if form.is_valid():

        new_comment = form.save(commit=False)
        new_comment.user = request.user
        new_comment.nickname = request.user.username
        new_comment.avatar = request.user.avator_sor
        new_comment.video = video
        new_comment.save()

        data = dict()
        data['nickname'] = request.user.username
        data['avatar'] = request.user.avator_sor
        data['timestamp'] = datetime.fromtimestamp(datetime.now().timestamp())
        data['content'] = new_comment.content

        comments = list()
        comments.append(data)
        comments = video.comment_set.order_by('-timestamp').all()
        comment_count = len(comments)
        html = render_to_string("comment/comment_single.html", {"comments": comments})
        return JsonResponse({"code":0, "html": html,"comment_count":comment_count})
    return JsonResponse({"code":1,'msg':'评论失败!'})

@csrf_exempt
def get_comments(request):
    if not request.is_ajax():
        return HttpResponseBadRequest()
    page = request.GET.get('page')
    page_size = request.GET.get('page_size')
    video_id = request.GET.get('video_id')
    video = get_object_or_404(ALLCoureslist, pk=video_id)
    comments = video.comment_set.order_by('-timestamp').all()
    comment_count = len(comments)

    code = 0
    html = render_to_string(
        "comment/comment_single.html", {"comments": comments})
    return JsonResponse({
        "code":code,
        "html": html,
        "comment_count": comment_count
    })