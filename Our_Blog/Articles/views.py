
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import  CreateArticleForm, CommentForm, ArticlesUpdateForm
from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import TemplateView, ListView
from .models import Blog_Articles, Category, Comment
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from django.db.models import Q




def index(request):
    post = Blog_Articles.objects.filter(Status='A')
    page = request.GET.get('page', 1)

    paginator = Paginator(post, 2)
    try:
        Blog_Posts = paginator.page(page)
    except PageNotAnInteger:
        Blog_Posts = paginator.page(1)
    except EmptyPage:
        Blog_Posts = paginator.page(paginator.num_pages)
    return render (request, 'index.html', {'Blog_Posts':Blog_Posts})



def CreateArticles(request):     
    if request.method == 'POST':
        form = CreateArticleForm(request.POST, request.FILES)
        if form.is_valid():
            pst = form.save(commit=False)
            pst.author = request.user
            pst.save()
            messages.success(request, ' Your Created Successfully. It will be approved soon ')
    else:
        form = CreateArticleForm()

    return render (request, 'create_article.html', {'form':form})    

def About(request):
    return render (request, 'about.html')





def Blog_Articles_By_Category(request, id):

    category = Category.objects.get(id=id)
    categorical_articles = Blog_Articles.objects.filter(Categorry=category)

    page = request.GET.get('page', 1)
    paginator = Paginator(categorical_articles, 2)
    try:
        Blog_Posts = paginator.page(page)
    except PageNotAnInteger:
        Blog_Posts = paginator.page(1)
    except EmptyPage:
        Blog_Posts = paginator.page(paginator.num_pages)
    return render (request, 'travel.html', {'Blog_Posts':Blog_Posts})




def Full_Article(request, id):

    post = get_object_or_404(Blog_Articles, id=id)
    comments = post.commentss.filter(parent = None)
    #comments = post.commentss.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():

            parent_obj = None
                        
            try:
                parent_id = int(request.POST.get('comment_id'))
            except:
                parent_id = None
    
            if parent_id:
                parent_obj = Comment.objects.get(id=parent_id)
                
                if parent_obj:                  
                    replay_comment = comment_form.save(commit=False)
                    replay_comment.parent = parent_obj
            
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.article = post
            new_comment.save()

    else:
        comment_form = CommentForm()

    return render(request, 'single.html', {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})


def Update_Articles(request, id): 
    article = get_object_or_404(Blog_Articles, id=id)
    if request.method == 'POST':
        form = ArticlesUpdateForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            messages.success(request, ' Your Article Updated successfully ')
    else:
        form = ArticlesUpdateForm(instance=article)
    return render(request, 'UpdateArticle.html', {'form':form})




def Delete_Articles(request, id):

    article = Blog_Articles.objects.get(id=id)
    article.delete()   
    return redirect('profile')


class SearchResultsView(ListView):
    model = Blog_Articles
    template_name = 'searchView.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Blog_Articles.objects.filter(
            Q(Title__icontains=query) | Q(Description__icontains=query)
        )
        return object_list

