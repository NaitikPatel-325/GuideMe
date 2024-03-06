from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from .forms import CustomUserCreationForm,LoginForm;
# Create your views here.
def home(request):
    return render(request, 'index.html')

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
            if user is not None:
                # print('user is not none')
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid login credentials') 
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            print('form is valid')
            user = form.save()
            login(request, user)
            print('user created' + user.username)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
        print(form.errors)  # Move the print statement here

    return render(request, 'register.html', {'form': form})
 