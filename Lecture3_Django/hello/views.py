from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'hello/index.html')
    # return HttpResponse("Hello, world. You're at the polls index.")

def users(request):
    return HttpResponse("Hello, User.")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")