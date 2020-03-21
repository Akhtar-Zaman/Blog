
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from .models import articles, Category
from .forms import CommentForm, PostForm, CreateArticleForm
    


def index(request):
    po = Category.objects.all()
    post = articles.objects.all()



    page = request.GET.get('page', 1)
    paginator = Paginator(post, 2)

    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, "blog.html", {'users': users, 'ak':po})


class SearchResultsView(ListView):
    model = articles
    template_name = 'search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = articles.objects.filter(
            Q(title__icontains=query) | Q(body__icontains=query)
        )
        return object_list
 

def catagoricalview(request, slug):
 
    aa = Category.objects.get(slug=slug)
    cat = articles.objects.filter(category = aa)
    return render(request, "catagory.html", { 'article':Category.objects.all(), 'akhtar': cat })

"""@login_required(login_url="/accounts/signin/")
def CreateArticle(request):
        posts=articles()
        if request.method == 'POST':
            post=articles()
            post.title= request.POST.get('title')
            post.slug= request.POST.get('slug')
            post.body= request.POST.get('body')
            post.image= request.POST.get('image')
            

            if post:
                post.author = request.user
                post.save()               
                return redirect('index')  

        else:
            return render(request, "create_article.html", {'form':posts})"""

@login_required(login_url="/accounts/signin/")
def CreateArticle(request): 
    pst = articles.objects.all()
    if request.method == 'POST':
        form = CreateArticleForm(request.POST)
        if form.is_valid():
            pst = form.save(commit=False)
            pst.author = request.user
            pst.save()
            return redirect('index')

    else:
        form = CreateArticleForm()
    return render(request, 'create_article.html', {'form':form})

"""def article_details(request, slug): 
    article = articles.objects.get(slug=slug)   
    return render(request, "article_details.html", {'article':article})"""


def article_details(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(articles, slug=slug)

    comments = post.comments.all()
    #comments = post.comments.filter(active=True) this is taking permission for admin approval
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})



@login_required(login_url="/accounts/signin/")
def profile(request):
     logged_in_user = request.user
     logged_in_user_posts = articles.objects.filter(author=logged_in_user)
     return render(request, 'profile.html', {'posts': logged_in_user_posts})



@login_required(login_url="/accounts/signin/")
def Edit_Post(request, slug): 
    pst = get_object_or_404(articles, slug=slug)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=pst)
        if form.is_valid():
            pst = form.save(commit=False)
            pst.author = request.user
            pst.save()
        

    else:
        form = PostForm(instance=pst)
    return render(request, 'Edit_Articles.html', {'form':form})