from django.contrib import admin
from .models import User, UserJsonData

# Register your models here.

admin.site.register(User)
admin.site.register(UserJsonData)

