from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello World ! <br> Hello Mr Roman")

def blogs(request):
    return HttpResponse("Blogs Or Something ..")

def blogs_details(request,id):
    return HttpResponse("Blog Details ... or somethings " + id)
