from django.contrib import admin
from .models import CustomUser, Article, UserFavouriteArticle

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    fields = ['username', 'password']
    
admin.site.register(CustomUser, CustomUserAdmin)

class ArticleAdmin(admin.ModelAdmin):
    model = Article
    fields = ['title', 'author', 'synopsis', 'content']
    
admin.site.register(Article, ArticleAdmin)

class UserFavouriteArticleAdmin(admin.ModelAdmin):
    model = UserFavouriteArticle
    fields = ['user', 'article']
    
admin.site.register(UserFavouriteArticle, UserFavouriteArticleAdmin)
