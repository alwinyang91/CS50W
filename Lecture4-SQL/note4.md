
---
---
# 1. Add new function for flights application
1. Got to urls.py to create a new path
```python
from django.urls import path
from . import views
app_name = "flights"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:flight_id>", views.flight, name="flight"),
    path("<int:flight_id>/books", views.book, name="book")
]
```
2. Add the view to views.py
```python
from django.shortcuts import render
from .models import Flight, Passenger
from django.http import HttpResponseRedirect
from django.urls import reverse

def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger_id = int(request.POST["passenger"])
        passenger = Passenger.objects.get(pk=passenger_id)
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight", args=(flight_id,)))

```

3. Create the form for the passenger in `flight.html`
```html

```
3.1 Modify the flight class view
```python
def flight(request, flight_id):
    # flight_id is the primary key of the flight
    flight = Flight.objects.get(pk=flight_id)
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all()
    })
```
