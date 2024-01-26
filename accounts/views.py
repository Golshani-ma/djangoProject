from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            print(request.user.username + " is authenticated Sucessfully")
            return redirect('/')
            # Redirect to a success page
        else:
            # Return an 'invalid login' error message
            print(request.user.username + "  is NOT authenticated")
    else:
        form = AuthenticationForm()
        context = {'form': form}
        return render(request, 'accounts/login.html', context)
        # Render the login form
def login_view_old(request):
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
    # test comments
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        form = UserCreationForm()
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)
    else:
        return redirect('/')
