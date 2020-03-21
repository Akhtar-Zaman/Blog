from django.db import models
from Accounts.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class articles(models.Model):
    title= models.CharField(max_length=300, unique=True)
    slug = models.SlugField(unique=True)
    body= models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='default.jpeg', blank=True)
    category = models.ForeignKey('Category', blank=True,  on_delete = models.CASCADE)
    author = models.ForeignKey(CustomUser, default= None, on_delete = models.CASCADE)
    

    def __str__(self):
        return self.title

    
    def snippet(self):
        return self.body[:50]+'.......'


class Comment(models.Model):
    post = models.ForeignKey(articles,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    #active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.name