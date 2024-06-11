
---
---
# 1. Modify the airline application

1. add path to the `urls.py` in `flights` floder
```zsh
cd flights
touch urls.py
cd ..
```
```python
from django.urls import path
from . import views

app_name = "flights"

urlpatterns = [
    path("", views.index, name="index")
]
```

2. add view to the `views.py` in `flights` floder
```python
from django.shortcuts import render
from .models import Flight

def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })
```

3. Create the `templates` and `static` folders for htmls
```zsh
cd flights
mkdir templates
cd templates
mkdir flights
cd flights
touch layout.html
touch index.html
cd ..
cd ..
mkdir static
cd static
mkdir flights
cd flights
touch styles.css
cd ..
cd ..
cd ..
```

---
---
# 2. Modify the html files and run server
```zsh
cd airline
python manage.py runserver
```
#### Then you can visit host:port/flights


---
---
# 3. Update or add data to the database
```zsh
cd airline
python manage.py shell
```
```python
from flights.models import *
Airport.objects.filter(city="New York")
Airport.objects.filter(city="New York").first()
# only get one reslut, if it has two or no results with error
jfk = Airport.objects.get(city="New York")
cdg = Airport.objects.get(city="Paris")
f = Flight(origin=jfk, destination=cdg, duration=435)
f.save()
f
```
#### Then if you refresh the page, the list is updated

---
---
# 4. Use Django admin app for modifing the database
1. In order to use the admin app, we first need to create an administrative account
```zsh
python manage.py createsuperuser
zewenreal@gmail.com
yang1512
```

2. Modify the `admin.py` file in `flights` folder
```python
from django.contrib import admin
from .models import Airport, Flight


# Register your models here.
admin.site.register(Airport)
admin.site.register(Flight)
```
#### Then you can to go host:post/admin

---
---
# 5. Create dynamic pages for each flight
1. Got to urls.py to create a new path
```python
from django.urls import path
from . import views
app_name = "flights"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:flight_id>", views.flight, name="flight"),

]
```
2. Add the view to views.py
```python
from django.shortcuts import render
from .models import Flight

# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })
# flight_id is given when visting the path /flights/flight_id
def flight(request, flight_id):
    # flight_id is the primary key of the flight
    flight = Flight.objects.get(pk=flight_id)
    return render(request, "flights/flight.html", {
        "flight": flight
    })
```

3. Create the `templates/flights/flight.html`

---
---
# 6. Make new data class
1. Create a new class called `Passenger` in `models.py`
```python
class Passenger(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    # blank=True allows passenger to be empty
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
```
2. make migrations
```dash
python manage.py makemigrations
```
3. Apply the changes in the database and create the new tables
```dash
python manage.py migrate
```
4. Go to admin.py add Passenger
```python
from django.contrib import admin
from .models import Airport, Flight, Passenger

# Register your models here.
admin.site.register(Airport)
admin.site.register(Flight)
admin.site.register(Passenger)
```

5. Modify the flight view
```python
def flight(request, flight_id):
    # flight_id is the primary key of the flight
    flight = Flight.objects.get(pk=flight_id)
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all()
    })
```
6. Modify the flight.html
7. Modify the index.html