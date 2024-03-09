from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User,Guide

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'userType', 'phone_number', 'profile_picture')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['userType'].required = False

    def clean_username(self):
        # If the username field is not intended to change, return the current username
        return self.instance.username

class GuideForm(forms.ModelForm):
    location = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter locations separated by commas'}),
        help_text='Enter the locations where you are available, separated by commas.'
    )
    expertise = forms.CharField()
    hourly_rate = forms.DecimalField(max_digits=5, decimal_places=2)
    available_for_hire = forms.BooleanField()
    bio = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Guide
        fields = (  'bio', 'location', 'expertise', 'hourly_rate', 'available_for_hire')
        
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)