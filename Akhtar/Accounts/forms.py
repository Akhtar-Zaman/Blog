
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.core.exceptions import ValidationError

class CreateAccount(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('image','username','Full_Name', 'email', 'Age', 'Occupation','password1','password2')

    def clean_username(self):
        username = self.cleaned_data['username']
        qs = CustomUser.objects.filter(username=username)
        if qs.exists():
            raise ValidationError('username already exist')
        return username


class CreateAccountChange(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('Full_Name', 'email', 'Age', 'Occupation' )