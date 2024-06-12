
---
---
# 1. Create a new appliaction project
```dash
cd Lecture3_Django2
cd mysite
```

- Create an application named `newyear`
```dash
python manage.py startapp newyear
```

- In order to install the application into the project, we need to edit the `settings.py` file
```python
INSTALLED_APPS = [
    "hello2",
    "newyear",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
```

- To create a URLconf in the `newyear` directory, create a file called `urls.py`. 
```dash
cd newyear
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

#### The next step is to point the root URLconf at the `newyear/urls` module. In `mysite/urls.py`, add an import for `django.urls.include` and insert an `include()` in the urlpatterns list, so you have:
```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("hello2/", include("hello2.urls")),
    path("newyear/", include("newyear.url")),
    path("admin/", admin.site.urls),
]
```

---
---
# 2. Write your view

- `newyear/views.py` is describe what it is the user sees when they visit a particular route

#### Let’s write the first view. Open the file `newyear/views.py` and put the following Python code in it:
```python
from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    # when the request is visited, newyear is already in the current route 
    return render(request, "newyear/index.html", {
        "newyear": now.month == 1 and now.day == 1
    })
```

---
---
# 3. Create the templates
```dash
cd newyear
mkdir templates
cd templates
mkdir newyear
cd newyear
touch index.html
cd ..
cd ..
```

---
---
# 4. Make style for HTML 
- you need to creat a static folder for storage scc files
```dash
cd newyear
mkdir static
cd static
mkdir newyear
cd newyear
touch styles.css
cd ..
cd ..
cd ..
```
- make `withstyle.html` file in `templates/newyear` folder
```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Is It New Year's?</title>
    </head>
    <body>
        {% if newyear %}
            <h1>YES</h1>
        {% else %}
            <h1>NO</h1>
        {% endif %}
    </body>
</html>
```

- add new view for `withstyle.html` in `views.py`
```python
def withstyle(request):
    now = datetime.datetime.now()
    # when the request is visited, newyear is already in the current route 
    return render(request, "newyear/withstyle.html", {
        "newyear": now.month == 1 and now.day == 1,
        # you can test it 
        # "newyear": True,
    })
```

- add new path for `withstyle.html` in `urls.py`
```python
urlpatterns = [
    path("", views.index, name="index"),
    path("withstyle", views.withstyle, name = "withstyle"),
]
```


#### Now HTML looks as
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Is It New Year's?</title>
        <link href="{% static 'newyear/styles.css' %}" rel="stylesheet">
    </head>
    <body>
        {% if newyear %}
            <h1>YES</h1>
        {% else %}
            <h1>NO</h1>
        {% endif %}
    </body>
</html>
```

