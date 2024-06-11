from django.db import models

# Create your models here.

# class Flight(models.Model):
#     origin = models.CharField(max_length=64)
#     destination = models.CharField(max_length=64)
#     duration = models.IntegerField()

#     def __str__(self):
#         return f"{self.id}: {self.origin} to {self.destination}"

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
    

class Passenger(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    # blank=True allows passenger to be empty
    # Flight.passengers can get all the passengers that have this flight
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"