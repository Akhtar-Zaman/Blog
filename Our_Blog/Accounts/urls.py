
from django.contrib.auth.views import PasswordResetCompleteView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetDoneView
from django.contrib.auth.views import PasswordResetView
from django.urls import path
from . import views






urlpatterns = [
  
    path('create-account/', views.CreateAccount, name='CreateAccount'),
    path('login/', views.Login, name='Login'),
    path('logout/', views.signout, name= "signout"),
    path('profile/', views.profile, name= "profile"),
    path('change_password/', views.change_password, name= "change_password"),
    path('activate/<uidb64>/<token>/',views.activate, name='activate'),
    path('reset-password/', PasswordResetView.as_view(), name= "reset_password"),
    path('reset-password/done/', PasswordResetDoneView.as_view(), name= "password_reset_done"),
    path('reset-password/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name= "password_reset_confirm"),
    path('reset-password/complete/', PasswordResetCompleteView.as_view(), name= "password_reset_complete"),
    
    
]


