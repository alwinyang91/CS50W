
---
---
# 1. Single Page Applications

---
## 1.1 With all HTML elements
e.g., `single_page.html`

## 1.2 With Multiple Routes
e.g., singlepage1

- Create a Django project
```zsh
cd Lecture6_UI
django-admin startproject singlepage1
```

- Create an application
```zsh
cd singlepage1
python manage.py startapp singlepage
cd ..
```

- Install the application into the project, we need to edit the `settings.py` file
```python
INSTALLED_APPS = [
    "singlepage",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
```

- Add an import for singlepage application in `singlepage1/urls.py`
```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("singlepage.urls"))
]
```

- Write view functions in `singlepage/views.py`
```python
from django.shortcuts import render
from django.http import Http404, HttpResponse

# Create your views here.
def index(request):
    return render(request, "singlepage/index.html")

texts = ["section1.", "section2.", "section3."]

def section(request, num):
    if 1 <= num <= 3:
        return HttpResponse(texts[num - 1])
    else:
        raise Http404("No such section")
```

- Create a URLconf for view paths to `singlepage/urls.py`
```zsh
cd singlepage1/singlepage
touch urls.py
cd ..
```

```python
from django.urls import path
from . import views

app_name = "singlepage"
urlpatterns = [
    path("", views.index, name="index"),
    path("sections/<int:num>", views.section, name="section")
]
```

- create a `template` folder with the application `singlepage` folder with `index.html`
```dash
cd singlepage
mkdir templates
cd templates
mkdir singlepage
cd singlepage
touch index.html
cd ..
cd ..
cd ..
```

- write `index.html`

- run application
```zsh
cd singlepage1
python manage.py runserver
```

- try
http://127.0.0.1:8000/sections/1

Then you can see the api information of each section

- visit http://127.0.0.1:8000 

Then you can click the buttons 