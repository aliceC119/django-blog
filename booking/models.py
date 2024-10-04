from django.db import models
from django.utils import timezone

class Booking(models.Model):
    date = models.DateField()
    slots = models.PositiveIntegerField(default=15)

    def __str__(self):
        return f"Booking for {self.date} with {self.slots} slots left"

