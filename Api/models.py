# api/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    tokens = models.IntegerField(default=4000)
    
    def __str__(self):
        return self.username

class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.message
    
class Token(models.Model):
    token = models.CharField(max_length=255)
    user = models.ForeignKey(User,related_name ='alltokens', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.token