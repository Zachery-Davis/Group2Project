from django.shortcuts import render, redirect
from .form import *
from django.contrib.auth import login, logout
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
            return redirect("dashboardPage")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = RegisterForm()
    context = {"form": form}
    return render(request, "login_register.html", context)

# Login Page
def loginPage(request):
    if request.user.is_authenticated:
        return redirect("dashboardPage")
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("dashboardPage")
        else:
            messages.error(request, "Login failed. Ensure your credentials are correct and try again.")
    else:
        form = AuthenticationForm()
    context = {"page": "login"}
    return render(request, "login_register.html", context)

def logoutUser(request):
    logout(request)
    return redirect("loginPage")

# Dashboard Page 
def dashboardPage(request):
    context = {}
    return render(request, "dashboard.html", context)

# tree Page 
def treePage(request):
    context = {}
    return render(request, "tree.html", context)

# Account Page 
def accountPage(request):
    context = {}
    return render(request, "account.html", context)

# profile Page 
def profilePage(request):
    context = {}
    return render(request, "profile.html", context)