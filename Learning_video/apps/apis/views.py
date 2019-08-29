from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
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
    return JsonResponse(ret)

from django.views.generic import View
from apps.videos.models import Courese

class get_coureses(View):
    def get(self,request):
        page = int(request.GET.get("page", 1))
        pagesize = int(request.GET.get("pagesize", 15))
        offset = int(request.GET.get("offset", 0))

        coureses_list = Courese.objects.all()
        total = len(coureses_list)
        coureses_list = coureses_list.values('id','courese_name', 'num', 'content', 'level',)
        coureses_list = coureses_list[offset:offset + pagesize]
        # 格式是bootstrap-table要求的格式
        questions_dict = {'total': total, 'coureses_list': coureses_list}
        return JsonResponse(questions_dict, safe=False)

from django.views.generic import View
from apps.videos.models import Courese,Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class CouresList(View):
    def get(self,request):
        level = request.GET.get("level")
        tag = request.GET.get("tag")
        if tag:
            tag_id = Category.objects.filter(name=tag).first()
        print(tag)
        print(level)
        if level and tag:
            courses = Courese.objects.filter(level=level,tag_id=tag_id).all()
        elif level:
            courses = Courese.objects.filter(level=level).all()
        elif tag:
            courses = Courese.objects.filter(tag_id=tag_id).all()
        # tag_id = Category.objects.filter(name=request.GET.get("tag")).first().id
        # print(tag_id)
        coures_level = Courese.LEVEL_CHOICES
        coures_tag = Category.objects.all()
        paginator = Paginator(courses,15)
        page = int(request.GET.get("page", 1))
        # coureses_list = Courese.objects.all()
        # total = len(coureses_list)
        # coureses_list = coureses_list.values('id', 'courese_name', 'num', 'content', 'level','img','tag' )
        # level = Courese.LEVEL_CHOICES
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            contacts = paginator.page(1)
        except EmptyPage:
            contacts = paginator.page(paginator.num_pages)
        # 格式是bootstrap-table要求的格式
        return render(request,'courses/index.html',{'contacts':contacts,'coures_tag':coures_tag,'coures_level':coures_level})

    # def get(self,request):
    #     coureses_list = Courese.objects.values("level","tag")
    #     paginator = Paginator(coureses_list,15)
    #     page = int(request.GET.get("page", 1))
    #     category = int(request.GET.get("category_list",0))
    #     level = int(request.GET.get("level",0))
    #     if category:coureses_list = coureses_list.filter(tag=category)
    #     if level:coureses_list = coureses_list.filter(level=level)
    #
    #
    #     print(category)
    #     tag = Courese.LEVEL_CHOICES
    #     search = request.GET.get("search","")
    #     kwgs = {"category":category,"search":search,"tag":tag,"level":level}
    #
    #     return JsonResponse(kwgs)