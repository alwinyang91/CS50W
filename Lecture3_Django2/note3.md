
---
---
# 1. Create a new appliaction project
```dash
cd Lecture3_Django2
cd mysite
```

- Create an application named `tasks`
```dash
python manage.py startapp tasks
```

- Edit the `mystit/settings.py` file
```python
INSTALLED_APPS = [
    "hello2",
    "newyear",
    "tasks",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
```

- Edit the `mystit/urls.py` file
```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("hello2/", include("hello2.urls")),
    path("newyear/", include("newyear.url")),
    path("tasks/", include("tasks.urls")),
    path("admin/", admin.site.urls),
]
```

- Create the `urls.py` file
```dash
cd tasks
touch urls.py
cd ..
```
In the `tasks/urls.py` file include the following code:
```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
```
---
---
# 2. Create the templates
```dash
cd tasks
mkdir templates
cd templates
mkdir tasks
cd tasks
touch index.html
cd ..
cd ..
cd ..
```
---
---
# 3. Make style for HTML 
- you need to creat a static folder for storage scc files
```dash
cd tasks
mkdir static
cd static
mkdir tasks
cd tasks
touch styles.css
cd ..
cd ..
cd ..
```
---
---
# 4. Write your view

- `tasks/views.py` is describe what it is the user sees when they visit a particular route

#### Let’s write the first view. Open the file `tasks/views.py` and put the following Python code in it:
```python
from django.shortcuts import render

# create a global  variable to  store the the task list
tasks = ["foo", "bar", "bza"]

# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })

```
- define a new funciton `add` with html 
```python
from django.shortcuts import render

# create a global  variable to  store the the task list
tasks = ["foo", "bar", "bza"]

# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })

def add(request):
    return render(request, "tasks/add.html")
```
- add its path to `urls.py`
```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("/add", views.add, name="add"),
]
```

---
---
# 5. Make the webpage dynamical 
- create a `layout.html` file
```dash
cd tasks/templates/tasks
touch layout.html
cd ..
cd ..
cd ..
```
- add {% block YourBlockName %} in the `layout.html`
- inheritate the `layout.html` in other html files `index2.html` and `add2.html`, e.g.,
```html
{% extends "tasks/layout.html" %}

{% block mybody %}
    <h1>Tasks</h1>
    <ul>
        {% for task in tasks %}
            <li>{{ task }}</li>
        {% endfor %}
    </ul>
{% endblock %}
```

- add hyperlinks to html files with the path name, where `name="add2"`, e.g., 
```html
{% extends "tasks/layout.html" %}

{% block mybody %}
    <h1>Tasks</h1>
    <ul>
        {% for task in tasks %}
            <li>{{ task }}</li>
        {% endfor %}
    </ul>
    <a href="{% url 'add2' %}">Add a task</a>
{% endblock %}
```

- To prevent name collision, add `app_name="tasks"` in the `urls.py` 
  - then add tasks: in front of the url name, e.g.,
```html
{% extends "tasks/layout.html" %}

{% block mybody %}
    <h1>Tasks</h1>
    <ul>
        {% for task in tasks %}
            <li>{{ task }}</li>
        {% endfor %}
    </ul>
    <a href="{% url 'tasks:add2' %}">Add a task</a>
{% endblock %}
```
---
---
# 6. Submit tasks to index page
- use post `method` attribute to submit tasks to index page with `action` attribute in the form, e.g.,
```html
{% extends "tasks/layout.html" %}

{% block mybody %}

    <h1>Add Tasks</h1>
    
    <form action="{% url 'tasks:add2' %}" method="post">
        <input type="text" name="task">
        <input type="submit">
    </form>
    <a href="{% url 'tasks:index2' %}">Back to list</a>
{% endblock %}
```

- avoid CSRF: Cross-Site Request Forgery
  - add a hidden CSRF token in the form
```html
{% extends "tasks/layout.html" %}

{% block mybody %}

    <h1>Add Tasks</h1>
    
    <form action="{% url 'tasks:add2' %}" method="post">
        {% csrf_token %}
        <input type="text" name="task">
        <input type="submit">
    </form>
    <a href="{% url 'tasks:index2' %}">Back to list</a>
{% endblock %}
```
---
---
# 7. Use Django forms
- create a new class to represent the form in `views.py`
  - import django forms
  - create class function
```python
from django.shortcuts import render
from django import forms

# create a global  variable to  store the the task list
tasks = ["foo", "bar", "bza"]

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)
```
- add the `NewTaskForm` class named `myform` in add2 view
```python
def add2(request):
    return render(request, "tasks/add2.html", {
        "myfrom": NewTaskForm(),
    })
```

- replace `<input type="text" name="task">` using `{{ myfrom }}`
```html
{% extends "tasks/layout.html" %}

{% block mybody %}

    <h1>Add Tasks</h1>
    
    <form action="{% url 'tasks:add2' %}" method="post">
        {% csrf_token %}
        <!-- <input type="text" name="task">  -->
        <!-- Use the django form -->
        {{ myfrom }}
        <input type="submit">
    </form>
    <a href="{% url 'tasks:index2' %}">Back to list</a>
{% endblock %}
```

---
---
# 8. Add server-side validation
```python
def add2(request):
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
```

---
---
# 9. Redirect to the task list page
- import HttpResponseRedirect and reverse
```python
from django.http import HttpResponseRedirect
from django.urls import reverse
```
- add HttpRequestRedirect function to add2 view
``` python
def add2(request):
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
    return render(request, "tasks/add2.html", {
        "myfrom": NewTaskForm(),
        "success": True
    })
```

---
---
# 10. Store the individual using session data
- deleat the global variable tasks and put it in index function view
```python
def index2(request):
    # check if the tasks is not in requestion.session
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "tasks/index2.html", {
        "tasks": request.session["tasks"]
    })
```

- create a Django table in order to store the individual data
```dash
cd mysite
python manage.py migrate 
```

- modify add2 funciton view, replace the global variable `tasks.append(task)` 
```python
def add2(request):
    if request.method == "POST":
        # request.POST contains all the data from the form 
        form = NewTaskForm(request.POST)
        if form.is_valid():
            # form.cleaned_data can access all the data in the form 
            task = form.cleaned_data["task"]
            # replace the global variable tasks with seession variable
            request.session["tasks"] += [task]
            # tasks.append(task)

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
```




















