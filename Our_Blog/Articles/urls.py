

from django.urls import path
from . import views




urlpatterns = [
  
    path('index/', views.index, name='index'),
    path('about/', views.About, name='about'),
    path('createarticle/', views.CreateArticles, name='create'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    path('<int:id>/', views.Full_Article, name='FullArticle'),
    path('category/<int:id>/', views.Blog_Articles_By_Category, name='categoryView'),
    path('update/<int:id>/', views.Update_Articles, name='Update_Articles'),
    path('delete/<int:id>/', views.Delete_Articles, name='Delete_Articles'),
    
]
