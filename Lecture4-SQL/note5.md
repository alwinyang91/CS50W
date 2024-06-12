
---
---
# 1. Make a new application called users
- Create the users app
```zsh
cd airline
python manage.py startapp users
```

# 2. add the app to the `airline/settings.py` file
```python
INSTALLED_APPS = [
    "flights",
    "users",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
```

# 3. add path to the `airline/urls.py` file
```python
urlpatterns = [
    path("admin/", admin.site.urls),
    path("flights/", include("flights.urls")),
    path("users/", include("users.urls")),
]
```

# 4. create and edit the new `users/urls.py` file
```zsh
cd users
touch urls.py
```
```python
from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout")
]
```

# 5. edit the `users/views.py` file
```python
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "users/user.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "users/login.html", {
                "message": "Invalid credentials."
            })
    else:
        return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {
        "message": "Logged out."
    })
```

# 6. Create the `templates` and `static` folders for htmls
```zsh
cd users
mkdir templates
cd templates
mkdir users
cd users
touch layout.html
touch index.html
cd ..
cd ..
mkdir static
cd static
mkdir users
cd users
touch styles.css
cd ..
cd ..
cd ..
```


















