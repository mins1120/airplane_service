from django.db import models
from api.users.models import User

class Ticket(models.Model):
    departure = models.CharField(max_length=100)
    departure_airport = models.CharField(max_length=100)
    departure_airport_code = models.CharField(max_length=10)
    destination = models.CharField(max_length=100)
    destination_airport = models.CharField(max_length=100)
    destination_airport_code = models.CharField(max_length=10)
    departure_date = models.DateField()
    destination_date = models.DateField()
    departure_time = models.TimeField()
    destination_time = models.TimeField()
    duration = models.CharField(max_length=20)
    airline = models.CharField(max_length=100)
    flight_class = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
