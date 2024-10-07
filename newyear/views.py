from django.http import HttpResponse
from django.shortcuts import render
from newyear.templates.newyear.date import get_message

# from .date import get_message  # Uncomment if get_message is needed
#response needed to be imported.

# Create your views here.

#request =  http request user made access to the website
def index(request) :
    message = get_message()
    context = {"message": message}

    # render dont take message: message as argument, it takes context as argument
    return render(request,"newyear/index.html",context)#at the last emelment i can do {message: message}  to pass the message 
