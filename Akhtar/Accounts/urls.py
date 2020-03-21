from django.conf.urls import url
from . import views
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.views import PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetCompleteView



urlpatterns = [

    url(r'^signup/$', views.signup, name= "signup" ),
    url(r'^signin/$', views.signin, name= "signin"),
    url(r'^signout/$', views.signout, name= "signout"),
    url(r'^change_password/$', views.change_password, name= "change_password"),
    url(r'^reset-password/$', PasswordResetView.as_view(), name= "reset_password" ),
    url(r'^reset-password/done/$', PasswordResetDoneView.as_view(), name= "password_reset_done" ),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)$', PasswordResetConfirmView.as_view(), name= "password_reset_confirm" ),
    url(r'^reset-password/complete/$', PasswordResetCompleteView.as_view(), name= "password_reset_complete" ),
]