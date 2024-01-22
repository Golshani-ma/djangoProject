from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print(request.user.username +" Authenticated")
            return redirect("/")
        else:
            print("Not Authenticated")
    return render(request, 'accounts/login.html')


def logout_view(request):
    return render(request, 'accounts/logout.html')


def signup_view(request):
    return render(request, 'accounts/signup.html')
