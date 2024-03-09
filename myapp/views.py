from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from .forms import CustomUserCreationForm,LoginForm,GuideForm;

def home(request):
    context = {
        'is_authenticated': request.user.is_authenticated
    }

    if request.user.is_authenticated:
        context['userType'] = request.user.userType

    print(context)
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
            print(username, password)
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                # print('user is not none')
                login(request, user)
                messages.success(request, 'Successfully logged in!')
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
        # print('user createsdsxxd' )
        # print(form)
        if form.is_valid():
            print('form is valid')
            user = form.save()
            login(request, user)
            print('user created')
            if user.userType == 'guide':
                return redirect(request.get_full_path() + 'set_Guide_profile' ) 
            else:
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
    
    return render(request, 'User_Profile.html', {'user': user})

def Guide_Profile(request):
    guide = request.user.guide
    # print(guide)
    return render(request, 'Guide_Profile.html', {'guide': guide})
    
def logout_request(request):
    logout(request)
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
    if request.method == 'POST':
        form = GuideForm(request.POST, instance=guide)
        if form.is_valid():
            form.save()
            messages.success(request, 'Guide information updated successfully')
            return redirect('Guide_Profile')
        else:
            messages.error(request, 'Invalid guide information')
    else:
        form = GuideForm(instance=guide)
    return render(request, 'Guide_Profile.html', {'form': form})