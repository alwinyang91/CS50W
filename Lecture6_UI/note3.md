
---
---
# 2. Windows Properties

- window.scrollY + window.innerHeight = document.body.offsetHeight
- window.innerWidth

e.g., `scroll.html`

Check if the window is scrolled to the bottom of the document
```html
<script>

    window.onscroll = () => {

        if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
            document.querySelector('body').style.background = 'green';
        } else {
            document.querySelector('body').style.background = 'white';
        }

    };

</script>
```

---
---
# 3. Infinite Scroll
e.g., scroll

- Create a Django project
```zsh
cd Lecture6_UI
django-admin startproject scroll
```

- Create an application
```zsh
cd scroll
python manage.py startapp posts
cd ..
```

- Install the application into the project, we need to edit the `settings.py` file
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

- Add an import for `scroll` application in `scroll/scroll/urls.py`
```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("scroll.urls"))
]
```

- Create a URLconf for view paths to `scroll/posts/urls.py`
```zsh
cd scroll/posts
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

- Write view functions in `scroll/posts/views.py`
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


- create a `template` folder with the application `scroll` folder with `index.html`
```dash
cd scroll/posts
mkdir templates
cd templates
mkdir posts
cd posts
touch index.html
cd ..
cd ..
cd ..
```

- run application
```zsh
cd scroll
python manage.py runserver
```

- try
http://127.0.0.1:8000/posts?start=1&end=10

Then you can see the api information 

- write `index.html`

- visit http://127.0.0.1:8000 


