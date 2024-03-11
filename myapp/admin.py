from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,Guide,Booking

admin.site.register(User)
admin.site.register(Guide)
admin.site.register(Booking)