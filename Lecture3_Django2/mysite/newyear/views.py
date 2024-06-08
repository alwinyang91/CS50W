from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    # when the request is visited, newyear is already in the current route 
    return render(request, "newyear/index.html", {
        "newyear": now.month == 1 and now.day == 1,
        # you can test it 
        # "newyear": True,
    })

def withstyle(request):
    now = datetime.datetime.now()
    # when the request is visited, newyear is already in the current route 
    return render(request, "newyear/withstyle.html", {
        "newyear": now.month == 1 and now.day == 1,
        # you can test it 
        # "newyear": True,
    })