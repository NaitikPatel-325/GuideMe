from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,Guide,Booking

#  class CustomGuideAdmin(admin.ModelAdmin):
#     list_display = ('guide_id','guide_user', 'location', 'expertise', 'hourly_rate', 'available_for_hire')
#     search_fields = ('guide_user', 'location', 'expertise', 'hourly_rate', 'available_for_hire')
#     list_filter = ('location', 'expertise', 'hourly_rate', 'available_for_hire')    
    
admin.site.register(User)
admin.site.register(Guide)
admin.site.register(Booking)