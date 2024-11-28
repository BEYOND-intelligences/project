from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'peges/index.html',{'name':'ahmed','age':'6'})

def about (request):
     return render(request,'peges/about.html')


def base (request):
    return render(request,'templates/part/base.html' )

