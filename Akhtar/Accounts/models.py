from django.db import models
from django.contrib.auth.models import AbstractUser





class CustomUser(AbstractUser):
    image = models.ImageField(default='default.jpeg', blank=True)
    Full_Name = models.CharField(max_length=100 )
    email = models.EmailField(max_length=255)
    Age = models.IntegerField(default=0)
    Occupation = models.CharField(max_length=100 )
    
    def __str__(self):
        return self.username