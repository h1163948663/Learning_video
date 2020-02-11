from django.shortcuts import render,HttpResponse
import logging
def test(request):
    return render(request,'index.html')

def index(request):
    return render(request,'index.html')

def login(request):

    return render(request,'login.html')


from django.shortcuts import render


def page_not_found(request):
    return render(request, '403.html')


def page_permission_denied(request):
    return render(request, '404.html')


def page_inter_error(request):
    return render(request, '500.html')

def comment(request):
    return render(request,'')