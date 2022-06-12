from django.db import models
from django.utils import timezone

# Create your models here.
class Registration(models.Model):
	name = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	repassword = models.CharField(max_length=100)
 
class Login(models.Model):
	name = models.CharField(max_length=100)
	password = models.CharField(max_length=100)

class Tip(models.Model):
	content = models.TextField()
	author = models.CharField(max_length=100,blank=True,null=True)
	date = models.DateField(default=timezone.now)

class Vote(models.Model):
    id_tip = models.IntegerField()
    username = models.CharField(max_length=100)
    vote = models.IntegerField()