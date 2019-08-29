from django.shortcuts import render

# Create your views here.
def index(requestion):
    return render(requestion,'questions/index.html')