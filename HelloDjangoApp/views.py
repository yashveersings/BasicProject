from django.http import request
from django.shortcuts import render
from .forms import car
def home(request):
    form = car()
    path=r"C:\Users\IT\Desktop\210962098\BasicProject\HelloDjangoApp\templates\prog1.html"
    return render(request,path,{"form":form})

def result(request):
    c = request.GET["manufacturer"]
    p = request.GET["model"]
    path2=r"C:\Users\IT\Desktop\210962098\BasicProject\HelloDjangoApp\templates\prog1_result.html"
    return render(request,path2,{"manufacturer":c,"model":p})
