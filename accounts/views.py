from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    print(request.user.username + " is authenticated Sucessfully")
                    return redirect('/')
                else:
                    print(request.user.username + "  is NOT authenticated")

        form = AuthenticationForm()
        context = {'form': form}
        return render(request, 'accounts/login.html', context)
    else:
        return redirect('/')


@login_required(login_url='./login')
def logout_view(request):
    logout(request)
    return redirect('/')


def signup_view(request):
    return render(request, 'accounts/signup.html')
