from platform import uname_result
from django.shortcuts import redirect, render

# Create your views here.

from .models import AuthUser
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



def display_view(request):

    if request.user.is_authenticated:
        return redirect('home')
    else:
        # if request.method == "POST":
        #     print("POST")
        if "signup" in request.POST:
            if request.POST["name"] not in [i.name for i in AuthUser.objects.all()]:
                if len(request.POST["password"])>= 8: 

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
                else:
                    messages.success(request,"Password should be greater than 8 characters")
            else:
                messages.success(request,"Username is already taken by another user ")

        elif "login" in request.POST:
            uname=request.POST["name"]
            password=request.POST["password"]
         

            user = authenticate(request, username=uname, password=password)

            print(user)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                messages.success(request,"Username or Password is incorrect")



        return render(request, 'login.html', {})

def logout_view(request):
    logout(request)
    return redirect("home")

