from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import (
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

app_name = 'accounts'

urlpatterns = [
    # Login
    path('login', login_view, name='login'),
    # Logout
    path('logout', logout_view, name='logout'),
    # Registration form
    path('signup', signup_view, name='signup'),

    # Other URL patterns
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # path('login/', MyLoginView.as_view(redirect_authenticated_user=True), name='login'),
    # path('register/', RegisterView.as_view(), name='register'),
    # path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

]
