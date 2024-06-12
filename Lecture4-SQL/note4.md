
---
---
# 1. Add new function for flights application
- Got to urls.py to create a new path
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
- Add the view to views.py
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
        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))

```

- Create the form for the passenger in `flight.html`
```html
<h2>Add Passenger</h2>
    <form action="{% url 'flights:book' flight.id %}" method="post">
        {% csrf_token %}
        <select name="passenger" id="">
            {% for passenger in non_passengers %}
                <option value="{{ passenger.id}}">{{ passenger }}</option>
            {% endfor %}
        </select>
        <input type="submit">
    </form>
```
    1. Match URL Pattern: Django finds the URL pattern with the name 'book' within the 'flights' namespace: `'flights/<int:flight_id>/book'`.

    2. Substitute Arguments: Django substitutes the provided argument flight.id (e.g., 1) into the `<int:flight_id>` placeholder in the matched pattern.

    3. Generate URL: The final URL is /flights/1/book.


- Modify the flight class view 

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

---
---
# 2. Customize the admin app
```python
class FlightAdmin(admin.ModelAdmin):
    list_display = ("__str__", "duration")

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)
    

admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, PassengerAdmin)
```
