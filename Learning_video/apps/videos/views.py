from django.shortcuts import render
from django.shortcuts import render,HttpResponse
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from apps.videos.models import ALLCoureslist


def index(request):
    return render(request,'index.html')



class PythonVideos(LoginRequiredMixin,View):
    def get(self, request):
        all_coures = ALLCoureslist.objects.all()
        search = request.GET.get("search", "")
        kwgs = {"python_coures":all_coures,"search":search}
        return render(request,'courses/show.html',kwgs)

from apps.videos.models import Courese,Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class Coureses(View):
    def get(self,request):
        coureses_list = Courese.objects.all()
        paginator = Paginator(coureses_list,15)
        page = int(request.GET.get("page", 1))
        coures_tag = Category.objects.all()
        print(coures_tag)
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            contacts = paginator.page(1)
        except EmptyPage:
            contacts = paginator.page(paginator.num_pages)
        print(contacts)
        # 格式是bootstrap-table要求的格式
        coureses_dict = { 'contacts': contacts,'coures_tag':coures_tag,}
        return render(request,'courses/index.html',coureses_dict)

from apps.videos.models import Courese
from django.views.generic import DetailView
class CoureseDetail(LoginRequiredMixin,DetailView,View):
    model = Courese
    pk_url_kwarg = 'id'
    template_name = 'courses/show.html'
    context_object_name = "object"

    def get_context_data(self, **kwargs):
        courese = self.get_object()
        Courese_name = Courese.objects.filter(courese_name=courese.courese_name,content=courese.content,id=courese.id)[0]
        print(Courese_name)
        kwargs["my_courese"] = ALLCoureslist.objects.filter(coure_id=Courese_name.id)[0]
        print(kwargs)
        #Courese.objects.filter(courese_name=courese.courese_name,content=courese.content)
        return super().get_context_data(**kwargs)

    def get(self, request, *args, **kwargs):
        courese = self.get_object()
        Courese_name = Courese.objects.filter(courese_name=courese.courese_name, content=courese.content, id=courese.id)[0]
        Courese_list = ALLCoureslist.objects.filter(coure_id=Courese_name.id)

        courese_name = {'Courese_name':Courese_name,'Courese_list':Courese_list}
        print(Courese_name.tag)
        return render(request,'courses/show.html',courese_name)