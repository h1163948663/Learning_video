from django.shortcuts import render,HttpResponse
import logging
def test(request):
    return render(request,'index.html')

def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')