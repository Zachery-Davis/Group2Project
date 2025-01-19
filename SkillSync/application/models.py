from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True, null=True)
    phoneNumber = models.CharField(max_length=15, null=True, validators=[
            RegexValidator(
                regex=r'^\+?1?\-?\d{3}\-\d{3}-\d{4}$',
                message="Phone number must be entered in the format: '+1-123-456-7890'."
            )
        ])
    bio = models.TextField(null=True)

    Linkedin = models.CharField(max_length=100, blank=True, null=True)
    Github = models.CharField(max_length=100, blank=True, null=True)

    avatar = models.ImageField(null=True, default="defaultUser.png")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

class UserJsonData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="json_data")
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    public = models.BooleanField(default=False)
    data = models.JSONField()

    


