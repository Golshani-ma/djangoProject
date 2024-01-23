from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect


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


def logout_view(request):
    return render(request, 'accounts/logout.html')


def signup_view(request):
    return render(request, 'accounts/signup.html')
