from django.shortcuts import render,HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from apps.videos.models import ALLCoureslist


def index(request):
    return render(request,'index.html')

from apps.videos.models import Courese
from django.views.generic import DetailView
from django.views import generic
from apps.videos.forms import CommentForm
class CoureseDetail(LoginRequiredMixin,DetailView,View):
    model = Courese
    pk_url_kwarg = 'id'
    template_name = 'courses/show.html'
    context_object_name = "object"

    def get_object(self, queryset=None):
        obj = super().get_object()
        obj.increase_view_count()
        return obj
    def get_context_data(self, **kwargs):
        courese = self.get_object()
        context = super(CoureseDetail, self).get_context_data(**kwargs)
        form = CommentForm()
        context["form"] = form
        Courese_name = Courese.objects.filter(courese_name=courese.courese_name,content=courese.content,id=courese.id)[0]
        # print(Courese_name)
        context["my_courese"] = ALLCoureslist.objects.filter(coure_id=Courese_name.id)[0]
        print(kwargs)
        return context

    def get(self, request, *args, **kwargs):
        courese = self.get_object()
        Courese_name = Courese.objects.filter(courese_name=courese.courese_name, content=courese.content, id=courese.id)[0]
        Courese_list = ALLCoureslist.objects.filter(coure_id=Courese_name.id)
        Courese_list_first = ALLCoureslist.objects.filter(coure_id=Courese_name.id)[0]
        # print(Courese_list_first)
        form = CommentForm()
        courese_name = {'Courese_name':Courese_name,'Courese_list':Courese_list,'Courese_list_first':Courese_list_first,'form':form}
        # print(Courese_name)



        return render(request,'courses/show.html',courese_name)


from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from apps.apis.views import ajax_required
from django.http import JsonResponse
@csrf_exempt
@ajax_required
@require_http_methods(["POST"])
def choose_video(request):
    if not request.user.is_authenticated:
        return JsonResponse({"code": 1, "msg": "请先登录"})

    video_link = request.POST['video_id_link']

    return JsonResponse({"code": 0, "video_link": video_link})

