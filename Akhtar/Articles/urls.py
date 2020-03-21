from django.conf.urls import url
from . import views



urlpatterns = [

    url(r'^index/$', views.index, name="index" ),
    url(r'^create_article/$', views.CreateArticle, name= "CreateArticle"),
    url(r'^search/$', views.SearchResultsView.as_view(), name='search_results'),
    url(r'^profile/$', views.profile, name= "profile"),
    url(r'^category/(?P<slug>[\w-]+)/$', views.catagoricalview, name= "catagoricalview"),
    url(r'^aa/(?P<slug>[\w-]+)/$', views.Edit_Post),
     url(r'^(?P<slug>[\w-]+)/$', views.article_details, name="article_details"),
    
    
]


