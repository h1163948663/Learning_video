
# Create your views here.

from django.contrib.auth.decorators import login_required
from django.shortcuts import render,reverse,redirect
from django.shortcuts import HttpResponse
from django.contrib import auth
# Create your views here.
from django.shortcuts import render
from django.views.generic import View
import logging
from django.contrib.auth.hashers import make_password
from .models import User
from django.http import JsonResponse
from .forms import LoginForm,RegisterForm
logger = logging.getLogger('account')

def test(request):
    return render(request,"index.html")
# Create your views here.

class Register(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, "user/register.html", {"form":form})
        # Ajax提交表单

    def post(self, request):
        from django.core.cache import cache
        ret = {"status": 400, "msg": "调用方式错误"}
        if request.is_ajax():
            form = RegisterForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password"]
                mobile = form.cleaned_data["mobile"]
                mobile_captcha = form.cleaned_data["mobile_captcha"]
                mobile_captcha_reids = cache.get(mobile)
                if mobile_captcha == mobile_captcha_reids:
                    user = User.objects.create(username=username, password=make_password(password))
                    user.save()
                    ret['status'] = 200
                    ret['msg'] = "注册成功"
                    logger.debug(f"新用户{user}注册成功！")
                    user = auth.authenticate(username=username, password=password)
                    if user is not None and user.is_active:
                        auth.login(request, user)
                        logger.debug(f"新用户{user}登录成功")
                    else:
                        logger.error(f"新用户{user}登录失败")
                else:
                    # 验证码错误
                    ret['status'] = 401
                    ret['msg'] = "验证码错误或过期"
            else:
                ret['status'] = 402
                ret['msg'] = form.errors
        logger.debug(f"用户注册结果：{ret}")
        return JsonResponse(ret)

from django.contrib.auth.mixins import LoginRequiredMixin
import json
from apps.apis.views import check_captcha
from django.views.decorators.csrf import csrf_exempt
class Login(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect(reverse('index'))
        form = LoginForm()
        request.session["next"] =  request.GET.get('next',reverse('index'))
        return render(request, "login.html", {"form":form})
    def post(self, request):
        form = LoginForm(request.POST)
        post_captcha_code = request.POST.get('captcha')
        session_captcha_code = request.session['captcha_code']
        print(post_captcha_code)
        print(session_captcha_code)
        if post_captcha_code.lower() == session_captcha_code.lower():
            if form.is_valid():
                username = form.cleaned_data["username"]
                user, flag = form.check_password()
                print(user, flag)
                print(user.is_active)
                if user is not None and flag == True:
                    auth.login(request, user)
                    logger.info(f"{user.username}登录成功")
                        # 跳转到next
                    return redirect(request.session.get("next", '/'))
                else:
                    msg = "用户名或密码错误"
                    logger.error(f"{username}登录失败, 用户名或密码错误")
            else:
                msg = "用户名不存在"
                logger.error(form.errors)
                logger.error(msg)
        else:
            msg = '验证码错误'
            logger.error(f"验证码错误")
        return render(request, "login.html", {"form": form, "msg": msg})


def logout(request):
    if request.session.get("user"):
        del request.session["user"]
    auth.logout(request)
    return redirect(reverse("index"))