from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    def __str__(self):
        return self.username

class ChatRoom(models.Model):
	name = models.CharField(max_length=128)
	def __str__(self):
		return self.name

class Message(models.Model):
	room = models.ForeignKey('ChatRoom', on_delete = models.CASCADE)
	user = models.ForeignKey('CustomUser', on_delete = models.CASCADE)
	msg = models.TextField()
	def __str__(self):
		return self.msg
