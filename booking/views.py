from django.shortcuts import render
from django.utils import timezone
from .forms import BookingForm
from .models import Booking
from django.contrib import messages

import calendar

# Create your views here.

def is_first_saturday(date):
    return date.weekday() == calendar.SATURDAY and 1 <= date.day <= 7

def booking_view(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking_date = timezone.now().replace(hour=12, minute=0, second=0, microsecond=0)
            if is_first_saturday(booking_date):
                if Booking.objects.filter(booking_date=booking_date).count() < 15:
                    booking = form.save(commit=False)
                    booking.booking_date = booking_date
                    booking.save()
                    messages.add_message(request, messages.SUCCESS, "Message received! I endeavour to respond within 2 working days.")
                    
                else:
                    form.add_error(None, 'Booking limit reached for this date.')
            else:
                form.add_error(None, 'Bookings are only allowed for the first Saturday of each month at 12 PM.')
    else:
        form = BookingForm()
    return render(request, 'booking/booking.html', {'form': form})

