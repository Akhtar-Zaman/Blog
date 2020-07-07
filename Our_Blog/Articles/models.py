

from Accounts.models import Custom_User_Model
from django.db import models





class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



STATUS_CHOICES = [
    ('A', 'Approved'),
]
class Blog_Articles(models.Model):
    Title= models.CharField(max_length=300, unique=True)
    Categorry = models.ForeignKey('Category', blank=True,  on_delete = models.CASCADE, null=True)
    Description = models.TextField()
    author = models.ForeignKey(Custom_User_Model, default= None, on_delete = models.CASCADE)
    Date = models.DateField(auto_now_add=True)
    Image = models.ImageField(default='default.jpeg', blank=True)   
    Status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    def __str__(self):
        return self.Title

    
    def snippet(self):
        return self.Description[:150]+'.......'


class Comment(models.Model):
    article = models.ForeignKey(Blog_Articles,on_delete=models.CASCADE, related_name='commentss')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='replies')

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.name