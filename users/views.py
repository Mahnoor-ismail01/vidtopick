from django.shortcuts import redirect, render

# Create your views here.

from .models import AuthUser
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout



def display_view(request):

    if request.user.is_authenticated:
        return redirect('home')
    else:
        # if request.method == "POST":
        #     print("POST")
        if "signup" in request.POST:
            USER = User.objects.create_user(
                        username=request.POST["name"],
                        password=request.POST["password"],
                        email=request.POST["email"]
                    )
            AuthUser.objects.create(
                name=request.POST["name"],
                email=request.POST["email"],
                user = USER
            )
            login(request, USER)
            return redirect("home")

        elif "login" in request.POST:
            email=request.POST["name"]
            password=request.POST["password"]
            print(email, password)

            user = authenticate(request, username=email, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect("home")

        return render(request, 'login.html', {})

def logout_view(request):
    logout(request)
    return redirect("home")

