from .models import Comment, articles
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

class CreateArticleForm(forms.ModelForm):
    class Meta:
        model = articles
        fields = ('title', 'slug', 'body', 'image', 'author', 'category')


class PostForm(forms.ModelForm):
    class Meta:
        model = articles
        fields = ('title', 'slug', 'body','category')