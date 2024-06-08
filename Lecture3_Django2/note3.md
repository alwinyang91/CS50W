
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
import datetime

# Create your views here.

```
