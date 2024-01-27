from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse


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
            messages.error(request, 'The User NotFound')
            # Return an 'invalid login' error message
            return HttpResponseRedirect(reverse('accounts:login'))
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


from accounts.forms import SignUpForm


def signup_view(request):
    # test comments
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('/')
        else:
            # Get Method
            form = SignUpForm()
            context = {'form': form}
            return render(request, 'accounts/signup.html', context)
    else:
        return redirect('/')
