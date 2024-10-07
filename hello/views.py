from django.http import HttpResponse
from django.shortcuts import render
#response needed to be imported.

# Create your views here.

#request =  http request user made access to the website
def index(request) :
    return render(request,"hello/index.html")

def brain(request):
    return HttpResponse("Hello, Brian!")

def david(request):
    return HttpResponse("Hello, David!")

def greet(request, name):
    return render(request,"hello/greet.html",{
         #name is a python dictionary to store names , name.capitalize() is a python function to capitalize the first letter of the name. and whne we type hello/name it will store in it.
        "name": name.capitalize()
    })
