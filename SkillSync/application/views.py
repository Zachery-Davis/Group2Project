from django.shortcuts import render, redirect
from .form import *
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


# Landing Page 
def landingPage(request):
    context = {}
    return render(request, "landing.html", context)

# Register Page 
def registerPage(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if(form.is_valid()):
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect("landingPage") # Will Be Sent To Home Page After Home Page Is Built
        else:
            messages.error(request, "The confirmation password does not match the password you entered. Please try again.")
    else:
        form = RegisterForm()
    context = {"type": "register"}
    return render(request, "login.html", context)

# Login Page
def loginPage(request):
    context = {"type": "login"}
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("landingPage") # Will Be Sent To Home Page After Home Page Is Built
        else:
            messages.error(request, "Login failed. Ensure your credentials are correct and try again.")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", context)

# Dashboard Page 
def dashboardPage(request):
    context = {}
    return render(request, "dashboard.html", context)

# Main Page 
def mainPage(request):
    context = {}
    return render(request, "main.html", context)

# Account Page 
def accountPage(request):
    context = {}
    return render(request, "account.html", context)

# profile Page 
def profilePage(request):
    context = {}
    return render(request, "profile.html", context)