from django.contrib import admin
from .models import Booking, Booking
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


@admin.register(Booking)
class AboutAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)
    list_display = ('date', 'name', 'email',)
