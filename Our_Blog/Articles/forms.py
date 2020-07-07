
from .models import Blog_Articles, Comment
from django import forms


class CreateArticleForm(forms.ModelForm):
    class Meta:
        model = Blog_Articles
        fields = ('Title', 'Description', 'Image', 'Categorry')

        widgets = {
            
            'Title': forms.TextInput(attrs={'class': 'input--style-6'}),
            'Description': forms.Textarea(attrs={'class': 'textarea--style-6'}),
            'Categorry': forms.Select(attrs={'class': 'value'}),
            'Image': forms.FileInput(attrs={'id': 'chooseFile'}),
        }

        def clean_Title(self):
            Title = self.cleaned_data['Title']
            qs = Custom_User_Model.objects.filter(Title=Title)
            if qs.exists():
                raise forms.ValidationError('Thsi Title already been used. Please try another')
            return Title



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

        widgets = {
            
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            
        }


class ArticlesUpdateForm(forms.ModelForm):
    class Meta:
        model = Blog_Articles
        fields = ('Title', 'Description', 'Image', 'Categorry')