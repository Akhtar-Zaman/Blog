
from django.contrib.auth.models import AbstractUser
from django.db import models


class Custom_User_Model(AbstractUser):

    Full_Name = models.CharField(max_length=100 )
    email = models.EmailField(max_length=255, unique=True)
    Age = models.IntegerField(null=True)
    Occupation = models.CharField(max_length=100 )
    Image = models.ImageField(default='default.jpeg', blank=True)
    
    def __str__(self):
        return self.username