from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

# create a global  variable to  store the the task list
tasks = ["foo", "bar", "bza"]

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    # priority = forms.IntegerField(label="Priority", min_value=1, max_value=5)


# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })

def add(request):
    return render(request, "tasks/add.html", {
        "tasks": tasks
    })


def index2_useGlobalVariable(request):
    return render(request, "tasks/index2.html", {
        "tasks": tasks
    })

def index2(request):
    # check if the tasks is not in requestion.session
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "tasks/index2.html", {
        "tasks": request.session["tasks"]
    })

def add2_canReturnDjangoForm(request):
    return render(request, "tasks/add2.html", {
        "myfrom": NewTaskForm(),
    })

def add2_canServerVaildation(request):
    if request.method == "POST":
        # request.POST contains all the data from the form 
        form = NewTaskForm(request.POST)
        if form.is_valid():
            # form.cleaned_data can access all the data in the form 
            task = form.cleaned_data["task"]
            tasks.append(task)
        else:
            return render(request, "tasks/add2.html", {
                # reture the form use made and it can show error as well 
                "myfrom": form
            })
    return render(request, "tasks/add2.html", {
        "myfrom": NewTaskForm(),
        "success": True
    })


def add2_useGlobalVariable(request):
    if request.method == "POST":
        # request.POST contains all the data from the form 
        form = NewTaskForm(request.POST)
        if form.is_valid():
            # form.cleaned_data can access all the data in the form 
            task = form.cleaned_data["task"]
            tasks.append(task)

            # returen to the index2 page
            return HttpResponseRedirect(reverse("tasks:index2"))
        else:
            return render(request, "tasks/add2.html", {
                # reture the form use made and it can show error as well 
                "myfrom": form
            })
    else:
        return render(request, "tasks/add2.html", {
            "myfrom": NewTaskForm(),
            "success": True
    })

def add2(request):
    if request.method == "POST":
        # request.POST contains all the data from the form 
        form = NewTaskForm(request.POST)
        if form.is_valid():
            # form.cleaned_data can access all the data in the form 
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            # returen to the index2 page
            return HttpResponseRedirect(reverse("tasks:index2"))
        else:
            return render(request, "tasks/add2.html", {
                # reture the form use made and it can show error as well 
                "myfrom": form
            })
    else:
        return render(request, "tasks/add2.html", {
            "myfrom": NewTaskForm(),
            "success": True
    })