from django.shortcuts import render
from django.views.generic import DetailView
# Create your views here.
from apps.videos.models import ALLCoureslist,Courese
from django.contrib.auth.mixins import LoginRequiredMixin
def index(request):
    return render(request,'paths/index.html')
