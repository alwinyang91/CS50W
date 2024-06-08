from django.shortcuts import render


# create a global  variable to  store the the task list
tasks = ["foo", "bar", "bza"]

# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })