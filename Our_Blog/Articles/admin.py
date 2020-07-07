

from .models import Blog_Articles, Category, Comment
from django.contrib import admin





def Approval(modeladmin, request, queryset):
    queryset.update(Status='A')
Approval.short_description = "Mark selected articles as Approved"


class Blog_Articles_Admin(admin.ModelAdmin):
    model = Blog_Articles
    list_display = ['Title', 'Categorry', 'author', 'Status']
    actions = [Approval]


admin.site.register(Blog_Articles, Blog_Articles_Admin )
admin.site.register(Category)
admin.site.register(Comment)
