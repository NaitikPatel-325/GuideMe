from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from .models import Guide,Booking
from .forms import CustomUserCreationForm,LoginForm,GuideForm,BookingForm;

def home(request):
    context = {
        'is_authenticated': request.user.is_authenticated
    }

    if request.user.is_authenticated:
        context['userType'] = request.user.userType

    # print(context)
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        # print('i am in login post method')
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # print(username, password)
            user = authenticate(request, username=username, password=password)
            # print(user)
            if user is not None:
                # print('user is not none')
                login(request, user)
                messages.success(request, 'Logged In Succesfully')
                return redirect('home')
            else:
                print('user is none')
                messages.error(request, 'Invalid login credentials')
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        print('user createsdsxxd' )
        print(form.errors)
        if form.is_valid():
            print('form is valid')
            user = form.save()
            login(request, user)
            print('user created')
            if user.userType == 'guide':
                return redirect(request.get_full_path() + 'set_Guide_profile' ) 
            else:
                messages.success(request,'Registration Succesfully')
                return redirect('home')
        else:
            messages.error(request, 'Invalid registration credentials')
    else:
        form = CustomUserCreationForm()
        print(form.errors)  

    return render(request, 'register.html', {'form': form})

def set_Guide_profile(request):
    if request.method == 'POST':
        form = GuideForm(request.POST)
        if form.is_valid():
            guide_instance = form.save(commit=False)
            guide_instance.guide_user = request.user
            guide_instance.save()
            messages.success(request, 'Guide profile saved successfully')
            return redirect('home')  
        else:
            messages.error(request, 'Invalid guide profile information')
    else:
        form = GuideForm()

    return render(request, 'set_Guide_profile.html', {'form': form})

def User_Profile(request):
    user = request.user
    book = Booking.objects.filter(user__id=user.id)
    return render(request, 'User_Profile.html', {'user': user, 'book': book})

def Guide_Profile(request):
    guide = request.user.guide
    # print(guide)
    book = Booking.objects.filter(guide__id=guide.id)
    return render(request, 'Guide_Profile.html', {'guide': guide, 'book': book})
    
def logout_request(request):
    logout(request)
    messages.success(request, 'Logged Out Successfully')
    return redirect('home')

def update_user_info(request):
    user = request.user

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, instance=user)
        print(form.errors)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'User information updated successfully')
            return redirect('home')
        else:
            messages.error(request, 'Invalid user information')
    else:
        form = CustomUserCreationForm(instance=user)

    return render(request, 'update_user_info.html', {'form': form})

def update_guide_info(request):
    guide = request.user.guide
    user = request.user

    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST, instance=user)
        guide_form = GuideForm(request.POST, instance=guide)

        print(user_form.errors)
        print(guide_form.errors)
        if user_form.is_valid() and guide_form.is_valid():
            user_form.save()
            guide_form.save()
            login(request, user)
            messages.success(request, 'Guide information updated successfully')
            return redirect('home')
        else:
            messages.error(request, 'Invalid guide information')
    else:
        user_form = CustomUserCreationForm(instance=user)
        guide_form = GuideForm(instance=guide)

    return render(request, 'update_guide_info.html', {'user_form': user_form, 'guide_form': guide_form})

def pricing(request):
    user = request.user
    booking = None
    if(user.userType == 'guide'):
        guide_id = request.user.guide.id
        booking = Booking.objects.filter(guide__id=guide_id)
    guides = Guide.objects.all()
    context = {
        'user': user,
        'guides': guides,
        'booking': booking
    }
    print(user.userType)
    for guide in guides:
        print(guide.guide_user.id)
    return render(request, 'pricing.html', context)


def book_guide(request, guide_id):
    guide = Guide.objects.get(id=guide_id)
    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        print(form.errors)
        print(form)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.guide = guide  
            print(booking)
            booking.save()
            messages.success(request, 'Booking is successful')
            return redirect('home')  
    else:
        form = BookingForm()

    guide_locations = guide.location.split(',')

    context = {
        'form': form,
        'guide_locations': guide_locations,
    }

    return render(request, 'booking_template.html', context)

def accept_booking(request,booking_id):
    print(request.GET)
    booking = Booking.objects.get(booking_id=booking_id)
    booking.status = 'accepted'
    booking.save()
    messages.success(request,'Boking is Accepted')
    return redirect('pricing')

def reject_booking(request,booking_id):
    print(request.GET)
    booking = Booking.objects.get(booking_id=booking_id)
    booking.status = 'rejected'
    booking.save()
    messages.success(request,'Boking is rejected')
    return redirect('pricing')

def complete_booking(request,booking_id):
    print(request.GET)
    booking = Booking.objects.get(booking_id=booking_id)
    booking.status = 'completed'
    booking.save()
    return redirect('User_Profile')

def rejects_booking(request,booking_id):
    print(request.GET)
    booking = Booking.objects.get(booking_id=booking_id)
    booking.status = 'rejected'
    booking.save()
    return redirect('User_Profile')