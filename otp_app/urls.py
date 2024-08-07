# otp_validation/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from .views import index, signup, verify_email, resend_otp, signin, dashboard

urlpatterns = [
    path('', index, name='index'),
    path('signup/', signup, name='signup'),
    path('register/', signup, name='register'),
    path('verify-email/<username>/', verify_email, name='verify-email'),
    path('resend-otp/', resend_otp, name='resend-otp'),
    path('signin/', signin, name='signin'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Add this line
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
