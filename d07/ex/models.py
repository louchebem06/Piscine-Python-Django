from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.
class CustomUser(AbstractUser):
    pass

class Article(models.Model):
    title = models.CharField(max_length=64)
    author = models.ForeignKey('CustomUser', on_delete = models.CASCADE)
    created = models.DateTimeField(default=timezone.now)
    synopsis = models.CharField(max_length=312)
    content = models.TextField()
    
    def __str__(self):
        return self.title

class UserFavouriteArticle(models.Model):
    user = models.ForeignKey('CustomUser', on_delete = models.CASCADE)
    article = models.ForeignKey('Article', on_delete = models.CASCADE)
    
    def __str__(self):
        return self.article.title.__str__()

class Login(models.Model):
	name = models.CharField(max_length=100)
	password = models.CharField(max_length=100)

class Registration(models.Model):
	name = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	repassword = models.CharField(max_length=100)
