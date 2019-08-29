from django.shortcuts import render
from django.views.generic import DetailView
# Create your views here.
from apps.videos.models import PythonCoures,Courese
from django.contrib.auth.mixins import LoginRequiredMixin
def index(requestion):
    return render(requestion,'paths/index.html')


def greenhand(requestion):
    return render(requestion,'paths/show.html')

#
# class CourseDetail(LoginRequiredMixin,DetailView):
#     model = Courese
#     pk_url_kwarg = 'id'

from django.views.generic import View
class CouresList(View):
    def get(self,request):
    #     level = Courese.objects.filter(level=request.GET.get("name"))
    #     print(level)
    #     # tag = Category.objects.filter(name=request.GET.get("level"))
    #     paginator = Paginator(level, 15)
    #     page = int(request.GET.get("page", 1))
    #
    # # coureses_list = Courese.objects.all()
    # # total = len(coureses_list)
    # # coureses_list = coureses_list.values('id', 'courese_name', 'num', 'content', 'level','img','tag' )
    # #     level = Courese.LEVEL_CHOICES
    #     try:
    #         contacts = paginator.page(page)
    #     except PageNotAnInteger:
    #         # If page is not an integer, deliver first page.
    #         contacts = paginator.page(1)
    #     except EmptyPage:
    #         contacts = paginator.page(paginator.num_pages)
    #     # 格式是bootstrap-table要求的格式
    #     coureses_dict = {'contacts': contacts,  'level': level}
        return render(request, 'courses/index.html', )


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