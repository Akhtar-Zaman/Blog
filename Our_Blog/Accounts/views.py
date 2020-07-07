
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode 
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.encoding import force_bytes, force_text 
from django.contrib.auth import update_session_auth_hash
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from Articles.models import Blog_Articles
from .models import Custom_User_Model
from .forms import  CreateAccountForm
from django.http import HttpResponse 
from django.contrib import messages




UserModel = get_user_model()


def CreateAccount(request):

    if request.method == 'POST':
        form = CreateAccountForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.id)),
                'token': default_token_generator.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            messages.warning(request, ' Please confirm your email address to complete the registration ')
            
        
    else:
        form = CreateAccountForm()
    return render (request, 'create_account.html', {'form':form})

def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(id=uid)
    except(TypeError, ValueError, OverflowError, Custom_User_Model.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


def Login(request):
        if request.method == "POST":
            username = request.POST.get('Username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)        
            if user:
                login(request, user)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    return redirect('index')
            
            else:
                messages.error(request, 'Username & Password did not match ')
        return render (request, 'log.html')



def signout(request):
        logout(request)
        return redirect('index')


@login_required(login_url="/accounts/login/")        
def change_password(request):

    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user= request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('Login')
    else:
        form = PasswordChangeForm(user= request.user)
    return render(request, 'change_password.html', {'form': form})



def profile(request):

    user = request.user
    logedin_user_articles = Blog_Articles.objects.filter(author=user)
    return render(request, 'profile.html', {'logedin_user_articles':logedin_user_articles})