from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.decorators import login_required
from .forms import TaskForm
from django.contrib.auth import logout
from .models import*

from django.utils import timezone
from datetime import datetime


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task-list')  # Redirect to your main page after registration
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('task-list')  # Redirect to your main page
    else:
        form = UserLoginForm()
    return render(request, 'registration/login.html', {'form': form})





@login_required(login_url='login')
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task-list')
    else:
        form = TaskForm()
    return render(request, 'task_create.html', {'form': form})



@login_required(login_url='login')
def task_list(request):
    today = datetime.today().date()
    print(today)
    tasks = Task.objects.filter(user=request.user)

    context={'tasks': tasks, 'today': today}
    return render(request, 'task_list.html', context)



def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect to your login page




