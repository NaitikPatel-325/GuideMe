from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm;
# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def login(request):
    return render(request, 'login.html') 

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        print(form)
        if form.is_valid():
            user = form.save()
            # login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})   