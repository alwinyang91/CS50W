
---
---
# 0. Create a new Django project
```dash
cd Lecture4-SQL
django-admin startproject airline
```

---
## 0.1 Create a new application
```dash
cd aireline
python manage.py startapp flights
```
- add the app in the `airline/settings.py`
```python
# Application definition
INSTALLED_APPS = [
    "flights",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
```

- add path to the `airline/urls.py`
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("flights/", include("flights.urls"))
]
```

- create the `urls.py` in `flights` floder
```dash
cd flights
touch urls.py
cd ..
```
```python
from django.urls import path
from . import views

urlpatterns = [

]
```

---
---
# 1. Modify the `models.py` for database
A `model` is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. **Generally, each model maps to a single database table.**

The basics:

Each model is a Python class that subclasses `django.db.models.Model`.

Each attribute of the model represents a database field.

With all of this, Django gives you an automatically-generated database-access API; see Making queries.

- Create a Flight model in `flights/models.py`
```python
from django.db import models

# Create your models here.
class Flight(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    duration = models.IntegerField()
```

- Make migrations
```dash
python manage.py makemigrations
```

- apply the model to Django database
```dash
python manage.py migrate
```

---
---
# 2. Modify the database
1. Open up `db.sqlite3` files, edit it with SQL syntax
2. Enter Django's shell, where you can run Python commands
```dash
cd airline
python manage.py shell
```

```python
from flights.models import Flight
f = Flight(origin="New York", destination="London", duration=415)
f.save()
# to exit the shell
exit()
```

---
## 2.1 query all the flights
```python
Flight.objects.all()
```
#### Make `Flight.objects.all()` return a string represetation in the class `Flight()` in `models.py` file
```python
from django.db import models

# Create your models here.
class Flight(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"
```
Then you can run the shell
```python
from flights.models import Flight
flights = Flight.objects.all()
flights

flight = flights.first()
flight
flight.id
flight.origin
flight.duration

# new you can delete the flight, before you refer and modify the Flight model
flight.delete()
```

#### Or you can try
```python
from flights.models import Flight
Flight.objects.values_list()
Flight.objects.values_list("origin")
Flight.objects.values_list("origin", flat=True)
```

## 2.2 Make and refer anothe table for representing airports in `models.py`
```python
from django.db import models

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"

class Flight(models.Model):
    # refer the Airport table
    # the contraints on_delete=models.CASCADE when the flight is deleted also delete the corrsponsonding flight
    # the argument related_name is a way of accessing the relationship in reverse order
    # e.g., when I have an Airport has all the flight that the airport is the origin
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"
```

#### After change the models, you need to change the database
1. make migrations
```dash
python manage.py makemigrations
```
2. Apply the changes in the database and create the new tables
```dash
python manage.py migrate
```

#### Create the tables and Add data to the database
```dash
python manage.py shell
```
```python
# import all the models
from flights.models import *
jfk = Airport(code="JKF", city="New York")
jfk.save()
lhr = Airport(code="LHR", city="London")
lhr.save()
cdg = Airport(code="CDG", city="Paris")
cdg.save()
nrt = Airport(code="NRT", city="Tokyo")
nrt.save()
f = Flight(origin=jfk, destination=lhr, duration=415)
f.save()
f
f.origin
f.origin.city
f.origin.code
lhr.arrivals.all()
```


