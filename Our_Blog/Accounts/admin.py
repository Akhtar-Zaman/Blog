
from django.contrib.auth.admin import UserAdmin
from .models import Custom_User_Model
from django.contrib import admin





class Custom_User_Admin(UserAdmin):
    model = Custom_User_Model
    list_display = ['username', 'email', 'Age', 'Occupation']


admin.site.register(Custom_User_Model, Custom_User_Admin)
