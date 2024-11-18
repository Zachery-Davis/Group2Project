from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True, null=True)
    password = models.CharField(max_length=100)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "password"]


