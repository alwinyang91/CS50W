
---
---
# 0. Install Django
```dash
pip install Django
```

---
---
# 1. Create a new Django project
```dash
cd Lecture3_Django2
django-admin startproject mysite
```
## Let’s look at what startproject created:
```
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```
#### These files are:

- The outer mysite/ root directory is a container for your project. Its name doesn’t matter to Django; you can rename it to anything you like.

- `manage.py`: A command-line utility that lets you interact with this Django project in various ways. You can read all the details about `manage.py` in django-admin and `manage.py`.
  - we do not have to touch this file, because use `manage.py` to execute commands for the Django project

- `mysite/settings.py`: Settings/configuration for this Django project. Django settings will tell you all about how settings work.
  - we can add deatures to our applicaitons 
  - or make some modifications to how the application behaves

- `mysite/urls.py`: The URL declarations for this Django project; a “table of contents” of your Django-powered site. You can read more about URLs in URL dispatcher.
  - a table of contents for our web application, because there are a lot of urls and routes you can visit

- The inner mysite/ directory is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. mysite.urls).

- mysite/__init__.py: An empty file that tells Python that this directory should be considered a Python package. If you’re a Python beginner, read more about packages in the official Python docs.


- mysite/asgi.py: An entry-point for ASGI-compatible web servers to serve your project. See How to deploy with ASGI for more details.

- mysite/wsgi.py: An entry-point for WSGI-compatible web servers to serve your project. See How to deploy with WSGI for more details.

---
---
# 2. Create an application
- try:
```dash
cd mysite
python manage.py runserver 
```

- Create an application named `hello`
```dash
python manage.py startapp hello2
```
#### That’ll create a directory `hello`, which is laid out like this:
```
hello/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```
- In order to install the application into the project, we need to edit the `settings.py` file
```python
INSTALLED_APPS = [
    "hello2",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
```

---
---
# 3. Write your view

- `hello/views.py` is describe what it is the user sees when they visit a particular route

#### Let’s write the first view. Open the file `hello/views.py` and put the following Python code in it:
```python
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the hello index.")
```
So now, we need to tell the app when should you actually return this response, i.e., what URL is the user going to visit.

Then we need to create some URL configuaration, when a particual URL is visisted, then `index` function should run in order to return that particular HTTPresonse.

To call the view, we need to map it to a URL - and for this we need a URLconf.

To create a URLconf in the `hello` directory, create a file called `urls.py`. 
```dash
cd hello2
touch urls.py
cd ..
```
In the `hello/urls.py` file include the following code:
```python
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
```

#### The next step is to point the root URLconf at the `hello.urls` module. In `mysite/urls.py`, add an import for `django.urls.include` and insert an `include()` in the urlpatterns list, so you have:
```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("hello/", include("hello.urls")),
    path("admin/", admin.site.urls),
]
```

#### You have now wired an index view into the URLconf. Verify it’s working with the following command:
```dash
python manage.py runserver
```
Go to http://localhost:8000/hello/ in your browser, and you should see the text “Hello, world. You’re at the polls index.”, which you defined in the index view.

---
## 3.2 Make another example
- define a new view in `views.py` 
```python
def brian(request):
    return HttpResponse("Hello, Brian! You're at the brian index.")
```

- add url path to the `mysite/urls.py`
```python
urlpatterns = [
    path("", views.index, name="index"),
    path("brain", views.brain, name="brain"),
]
```

---
## 3.3 Make parameterize the path via certain converters
- define a new view function `greet` in `views.py`
```python
def greet(request, name):
    return HttpResponse(f"Hello, {name}!")
```
- add url path to `mysite/urls.py`
```python
urlpatterns = [
    path("", views.index, name="index"),
    path("brain", views.brain, name="brain"),
    path("<str:name>", view.greet, name="greet"),
]
```

---
---
# 4. Render a HttpResponse
- modify index function
```python
def index(request):
    # first arguement is httpRequest: request
    # second arguement is the name of the template: 'index.html'
    return render(request, 'hello/index.html')
```

- create a `template` folder with `hello` folder with `index.html`
```dash
cd hello2
mkdir templates
cd templates
mkdir hello2
cd hello2
touch index.html
```