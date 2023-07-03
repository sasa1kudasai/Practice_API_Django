from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Users(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField(unique=True, max_length=100)
    message = models.CharField(max_length=100, blank=True)
    owner = models.ForeignKey(User, related_name='users',
                              on_delete=models.CASCADE,
                              null=True)
    created_at = models.DateTimeField(auto_now_add=True)
