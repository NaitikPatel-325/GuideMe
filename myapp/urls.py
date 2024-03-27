from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('user_login/', views.user_login, name='user_login'),
    path('register/', views.register, name='register'),
    path('register/set_Guide_profile/', views.set_Guide_profile, name='set_Guide_profile'),
    path('User_Profile/', views.User_Profile, name='User_Profile'),
    path('Guide_Profile/', views.Guide_Profile, name='Guide_Profile'),
    path('logout/', views.logout_request, name='logout'),
    path('update_user_info/', views.update_user_info, name='update_user_info'),
    path('update_guide_info/', views.update_guide_info, name='update_guide_info'),
    path('pricing/', views.pricing, name='pricing'),
    path('book_guide/<int:guide_id>/', views.book_guide, name='book_guide'),
    path('pricing/accept_booking/', views.accept_booking, name='accept_booking'),
    path('accept_booking/<int:booking_id>/', views.accept_booking, name='accept_booking'),
    path('reject_booking/<int:booking_id>/', views.reject_booking, name='reject_booking'),
]
