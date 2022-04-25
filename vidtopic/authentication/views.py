from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def mainvid(request):
    return render(request, 'authentication/mainvid.html')

def afterlogin(request):
    return render(request, 'authentication/afterlogin.html')

def history(request):
    return render(request, 'authentication/history.html')

def favorites(request):
    return render(request, 'authentication/favorites.html')

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('mainvid')
    else:
        form = UserRegisterForm()

    return render(request, 'authentication/register.html', {'form': form})


@login_required()
def profile(request):
    return render(request, 'authentication/profile.html')
