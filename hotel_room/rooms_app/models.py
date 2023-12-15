from django.db import models

# Create your models here.
from django.contrib.auth.models import User
# Create your models here.
class Hotels(models.Model):
    name = models.CharField(max_length=30, default="Hayat")
    owner = models.CharField(max_length=20)
    location = models.CharField(max_length=50)
    state = models.CharField(max_length=50, default="kerala")
    country = models.CharField(max_length=50, default="india")
    owner_number =models.IntegerField(default=6238066012,null=True, blank=True)

    def __str__(self):
        return self.name


class HotelRoom(models.Model):
    ROOM_TYPE_CHOICES = [
        ('1BHK', '1BHK'),
        ('2BHK', '2BHK'),
        ('3BHK', '3BHK'),
    ]

    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE, related_name='rooms')
    room_number = models.CharField(max_length=10)
    image = models.ImageField(upload_to='room_images/')  # 'room_images/' is the upload directory
    price = models.IntegerField(default=5000)
    room_type = models.CharField(max_length=4, choices=ROOM_TYPE_CHOICES, default='1BHK')

    def __str__(self):
        return f"{self.hotel.name} - Room {self.room_number} ({self.get_room_type_display()})"


class Reservation(models.Model):

    check_in = models.DateField(auto_now =False)
    check_out = models.DateField(auto_now =False)
    booked_date = models.DateField(auto_now=True)
    room = models.ForeignKey(HotelRoom, on_delete = models.CASCADE)
    guest = models.ForeignKey(User, on_delete= models.CASCADE)
    num_guests = models.IntegerField(default=1)
    
    def __str__(self):
        return f"{self.guest.username} - {self.room.hotel.name} - Room {self.room.room_number}"
