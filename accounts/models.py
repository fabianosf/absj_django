# models.py

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    login = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    

    def __str__(self):
        return self.user.username
