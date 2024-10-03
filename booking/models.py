from django.db import models
from django.utils import timezone
# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    booking_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.booking_date}"