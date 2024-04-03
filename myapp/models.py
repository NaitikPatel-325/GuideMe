from django.contrib.auth.models import AbstractUser
from django.db import models

User_Choices = ( 
    ("guide", "Guide"), 
    ("user", "User"), 
) 
class User(AbstractUser):
    email = models.EmailField()
    userType = models.CharField( 
        max_length = 20, 
        choices = User_Choices, 
        default = "user",
    )
    profile_picture = models.ImageField(upload_to='static/img', blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True)


class Guide(models.Model):
    guide_user = models.OneToOneField(User, on_delete=models.CASCADE) 
    location = models.CharField(max_length=255, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='static/img', blank=True, null=True)
    expertise = models.CharField(max_length=100)
    hourly_rate = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    available_for_hire = models.BooleanField(default=False)
    bio = models.TextField(blank=True)
    
class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    guide = models.ForeignKey(Guide, on_delete=models.CASCADE)  
    date = models.DateField()
    hrs = models.IntegerField()
    location = models.CharField(max_length=255)
    status = models.CharField(max_length=20, default='pending')