from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    firstName = models.CharField(max_length=200, null=True)
    lastName = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(max_length=500, null=True)
    
    REQUIRED_FIELDS = ["firstName", "lastName", "email"]


