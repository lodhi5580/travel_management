from django.contrib.auth.models import User
from django.db import models

class Bus(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    bus_no = models.CharField(max_length=100)


    def __str__(self):
        return self.name

class Route(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()

    def __str__(self):
        return f"{self.source} to {self.destination}"
    


class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    seat_number = models.IntegerField()
    booking_date = models.DateTimeField(auto_now_add=True)
    price = models.FloatField()

    def __str__(self):
        return f"Ticket {self.id} for {self.user.username}"
