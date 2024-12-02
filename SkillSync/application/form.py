from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class UserForm(ModelForm):
    username = forms.CharField(max_length=150, required=False)
    email = forms.EmailField(required=False)
    password = forms.CharField(widget=forms.PasswordInput(), required=False)
    avatar = forms.ImageField(required=False)
    bio = forms.CharField(required=False, widget=forms.Textarea(attrs={
            'rows': 5, 
            'cols': 40,
        }))
    class Meta:
        model = User
        fields = ["username", "email", "password", "first_name", "last_name", "avatar", "bio"]

class TreeForm(forms.Form):
    name = forms.CharField(max_length=100)
    subject = forms.CharField(max_length=100)
    