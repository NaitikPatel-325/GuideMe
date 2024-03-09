from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,Guide

admin.site.register(User)
admin.site.register(Guide)