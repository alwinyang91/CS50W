from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    # first arguement is httpRequest: request
    # second arguement is the name of the template: 'index.html'
    # add folder hello in order to avoid conflict with other index.html
    return render(request, "hello2/index.html")

# def index(request):
#     return HttpResponse("Hello, world! You're at the hello index.")

def brian(request):
    return HttpResponse("Hello, Brian! You're at the brian index.")

def greet(request, name):
    # render can take third argument: content
    return render(request, "hello2/greet.html", {
        # so you can use the variable called name
        "name": name.capitalize()
    })

# def greet(request, name):
#     return HttpResponse(f"Hello, {name.capitalize()}!")