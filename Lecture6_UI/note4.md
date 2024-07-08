
---
---
# 4. Animation

- you can make grow animation,
e.g., `animate0.html`

- or move animation,
e.g., `animate1.html` and `animate2.html`

- you can also write a javascript to control the animation,
e.g., `animate3.html`

---
## 4.1 Hide Animation

e.g., `hide`

- Create a Django project
```zsh
cd Lecture6_UI
django-admin startproject hide
```

- Create an application
```zsh
cd hide
python manage.py startapp posts
cd ..
```

- Install the application into the project, we need to edit the `hide/hide/settings.py` file
```python
INSTALLED_APPS = [
    "posts",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
```

- Add an import for `posts` application in `hide/hide/urls.py`
```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("posts.urls"))
]
```

- Create a URLconf for view paths to `hide/posts/urls.py`
```zsh
cd hide/posts
touch urls.py
cd ..
cd ..
```

```python
from django.urls import path
from . import views

app_name = "posts"
urlpatterns = [
    path("", views.index, name="index"),
    path("posts", views.posts, name="posts")
]
```

- Write view functions in `hide/posts/views.py`
```python
from django.shortcuts import render
from django.http import JsonResponse
import time

# Create your views here.
def index(request):
    return render(request, "posts/index.html")

def posts(request):

    # Get start and end points
    start = int(request.GET.get("start") or 0)
    end = int(request.GET.get("end") or (start + 9))

    # Generate list of posts
    data = []
    for i in range(start, end + 1):
        data.append(f"Post #{i}")

    # Artificially delay speed of response
    time.sleep(1)

    # Return list of posts
    return JsonResponse({
        "posts": data
    })
```

- create a `template` folder with the application `hide` folder with `index.html`
```zsh
cd hide/posts
mkdir templates
cd templates
mkdir posts
cd posts
touch index.html
cd ..
cd ..
cd ..
cd ..
```

# 4.2 Improver the animations in `index.html`




- run application
```zsh
cd hide
python manage.py runserver
```










