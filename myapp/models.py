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
    profile_picture = models.ImageField(upload_to='user_profile_pics/', blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True)


class Guide(models.Model):
    guide_user = models.OneToOneField(User, on_delete=models.CASCADE) 
    location = models.CharField(max_length=255, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='guide_profile_pics/', blank=True, null=True)
    expertise = models.CharField(max_length=100)
    hourly_rate = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    available_for_hire = models.BooleanField(default=False)
    bio = models.TextField(blank=True)


class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    guide = models.ForeignKey(Guide, on_delete=models.CASCADE)  
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.CharField(max_length=20, default='pending')


# class Review(models.Model):
#     Review_id = models.IntegerField(primary_key = True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     guide = models.ForeignKey(Guide, on_delete=models.CASCADE)
#     rating = models.IntegerField()
#     comment = models.TextField()
#     date = models.DateTimeField(auto_now_add=True)

# class Message(models.Model):
#     Message_id = models.IntegerField(primary_key = True)
#     sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
#     receiver = models.ForeignKey(Guide, on_delete=models.CASCADE, related_name='received_messages')
#     content = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)
#     is_read = models.BooleanField(default=False)

# class Notification(models.Model):
#     Notification_id = models.IntegerField(primary_key=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     guide = models.ForeignKey(Guide, on_delete=models.CASCADE, null=True, blank=True)
#     message = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)
#     is_read = models.BooleanField(default=False)
