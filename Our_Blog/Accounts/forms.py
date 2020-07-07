
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Custom_User_Model
from django import forms






class CreateAccountForm(UserCreationForm):
    class Meta:
        model = Custom_User_Model
        fields = ('Image','Full_Name', 'username', 'email', 'Age','Occupation','password1', 'password2')
        
        widgets = {
	    'Image': forms.FileInput(attrs={'id': 'chooseFile'}),
	    'Full_Name': forms.TextInput(attrs={'class': 'input100'}),
	    'username': forms.TextInput(attrs={'class': 'input100'}),
	    'email': forms.EmailInput(attrs={'class': 'input100'}),
	    'Age': forms.TextInput(attrs={'class': 'input100'}),
	    'Occupation': forms.TextInput(attrs={'class': 'input100'}),
	    'password1': forms.PasswordInput(attrs={'class': 'input100'}),
	    'password2': forms.PasswordInput(attrs={'class': 'input100'}),
		}

    def clean_username(self):
        username = self.cleaned_data['username']
        qs = Custom_User_Model.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError('Thsi Username already been used')
        return username


    def clean_email(self):
        email = self.cleaned_data['email']
        qs = Custom_User_Model.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('This Email already been used')
        return email


