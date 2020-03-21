from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib import messages
from .forms import CreateAccount
from .models import CustomUser
from Articles.models import articles 
from django.contrib.auth import update_session_auth_hash


def signup(request):

    if request.method == 'POST':
        form = CreateAccount(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            Full_Name = form.cleaned_data['Full_Name']
            email = form.cleaned_data['email']
            Age = form.cleaned_data['Age']
            Occupation = form.cleaned_data['Occupation']
            password = form.cleaned_data['password1']
            user = CustomUser.objects.create_user(username=username,Full_Name=Full_Name, email=email, Age=Age, Occupation=Occupation, password=password)
            messages.success(request, 'Thanks for registering {}'.format(user.username))
            return redirect('signin')
    else:
        form = CreateAccount()
    return render(request, 'sign up.html', {'form': form})

# This function works for student Login
def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)        
        if user:
             login(request, user)
             if 'next' in request.POST:
               return redirect(request.POST.get('next'))
             else:
               return redirect('CreateArticle')
          
        else:
             return render(request, "sign in.html")
            
    else:
         return render(request, "sign in.html")


def signout(request):
     if request.method == "POST":
        logout(request)
        return redirect('index')



def change_password(request):

    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user= request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/articles/profile')
    else:
        form = PasswordChangeForm(user= request.user)
        return render(request, 'change_password.html', {'form': form})