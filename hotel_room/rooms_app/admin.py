from django.contrib import admin

# Register your models here.
from .models import Hotels,HotelRoom,Reservation
# Register your models here.
admin.site.register(Hotels)
admin.site.register(HotelRoom)
admin.site.register(Reservation)


