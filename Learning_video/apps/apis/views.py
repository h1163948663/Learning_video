from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse
from libs import sms
import random
import logging
from io import BytesIO
from libs import patcha
import base64
logger = logging.getLogger("apis")

# logger = logging.getLogger('sms')
def test(request):
    return HttpResponse("题库视图")

def get_mobile_captcha(request):
    ret = {"code": 200, "msg": "验证码发送成功！"}
    try:
        mobile = request.GET.get("mobile")
        if mobile is None: raise ValueError("手机号不能为空！")
        mobile_captcha = "".join(random.choices('0123456789', k=6))
        print(mobile_captcha)
        from django.core.cache import cache
        # 将短信验证码写入redis, 300s 过期
        cache.set(mobile, mobile_captcha, 300)
        if not sms.send_sms(mobile, mobile_captcha):
            raise ValueError('发送短信失败')
    except Exception as ex:
        logger.error(ex)
        ret = {"code": 400, "msg": "验证码发送失败！"}
    return JsonResponse(ret)

def get_captcha(request):
    # 直接在内存开辟一点空间存放临时生成的图片
    f = BytesIO()
    # 调用check_code生成照片和验证码
    img, code = patcha.create_validate_code()
    # 将验证码存在服务器的session中，用于校验
    request.session['captcha_code'] = code
    # 生成的图片放置于开辟的内存中
    img.save(f, 'PNG')
    # 将内存的数据读取出来，转化为base64格式
    ret_type = "data:image/jpg;base64,".encode()
    ret = ret_type+base64.encodebytes(f.getvalue())
    del f
    return HttpResponse(ret)

def check_captcha(request):
    ret = {"code":400, "msg":"验证码错误！"}
    post_captcha_code = request.GET.get('captcha_code')
    session_captcha_code = request.session['captcha_code']
    print(post_captcha_code, session_captcha_code)
    if post_captcha_code.lower() == session_captcha_code.lower():
        ret = {"code": 200, "msg": "验证码正确"}
        print(ret)
    return JsonResponse(ret)


from django.views.generic import View
from apps.videos.models import Courese,Category,Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class CouresList(View):
    def get(self,request):
        tag = request.GET.get("tag")
        order = request.GET.get("order")
        user = request.user
        if tag != 'all':
            if tag =='' or tag ==None:
                tag = 'all'
            if tag == 'C\C  ':
                tag="C\C++"
            tag_id = Tag.objects.filter(tag=tag).values('id')
            courses = Courese.objects.filter(tag=tag_id).all()
        else:
            courses = Courese.objects.all()
        if order == 'latest':
            courses = courses.order_by('create_time')
        if order == 'hotest':
            courses = courses.order_by('view_count').reverse()
        print(courses)
        coures_tag = Tag.objects.all()
        paginator = Paginator(courses,15)
        page = request.GET.get('page')
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            contacts = paginator.page(1)
        except EmptyPage:
            contacts = paginator.page(paginator.num_pages)
        coures_dict = {'contacts':contacts,'tag':tag,'coures_tag':coures_tag,'user':user,'order':order}
        return render(request,'courses/index.html',coures_dict)

class CoureseSearch(View):
    def get(self,request):
        search = request.GET.get("search",'')
        order = request.GET.get("order",'')
        user = request.user
        print(search)
        courese_list = None
        tag = 'all'
        if search:
            courese_list = Courese.objects.filter(courese_name__icontains=search)
        if order == 'latest':
            courese_list = courese_list.order_by('id')
        if order == 'hotest':
            courese_list = courese_list.order_by('view_count').reverse()
        paginator = Paginator(courese_list, 15)
        page = request.GET.get('page')
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            contacts = paginator.page(1)
        except EmptyPage:
            contacts = paginator.page(paginator.num_pages)
        coures_dict = {'contacts': contacts,'tag':tag,'search':search,'order':order}
        return render(request,'courses/index.html',coures_dict)

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from  django.http import HttpResponseBadRequest

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
@ajax_required
@require_http_methods(["POST"])
def collect(request):
    if not request.user.is_authenticated:
        return JsonResponse({"code": 1, "msg": "请先登录"})
    video_id = request.POST['video_id']
    print(video_id)
    video = Courese.objects.get(pk=video_id)
    print(video)
    user = request.user
    print(user)
    video.switch_collect(user)
    return JsonResponse({"code": 0, "user_collected": video.user_collected(user)})