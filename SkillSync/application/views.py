from django.shortcuts import render, redirect
from .form import *
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import UserJsonData
import os
import sys
cwd = os.getcwd()
apiPath = os.path.abspath(os.path.join(cwd, "../"))
sys.path.append(apiPath)
from api.ChatGPTAPI import ChatGPTAPI

# Access Key Path
apiKey = os.path.abspath(os.path.join(cwd, "../api/apiKey.txt"))



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
@login_required(login_url="login")
def dashboardPage(request):
    user = request.user
    trees = user.json_data.all()
    context = {"trees": trees}
    return render(request, "dashboard.html", context)

# Tree Page 
def treePage(request):
    user = request.user
    trees = user.json_data.all()
    tree = trees[0]
    jsonData = tree.data
    context = {"jsonData": jsonData}
    return render(request, "tree.html", context)

# Create Tree Page
def createTreePage(request):
    if request.method == "POST":
        form = TreeForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            api = ChatGPTAPI(apiKey, subject)
            title = api.titleOfTree()
            description = api.descriptionOfTree()
            newTree = UserJsonData(user=request.user, name=title, description=description, data=api.response)
            newTree.save()
            return redirect("dashboardPage")
    context = {}
    return render(request, "tree_form.html", context)

# Profile Page 
@login_required(login_url="login")
def profilePage(request, user):
    user = User.objects.get(username=user)
    trees = user.json_data.all()
    context = {"user": user, "trees": trees}
    return render(request, "profile.html", context)

# Update User Page 
@login_required(login_url="login")
def updateUserPage(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            if form.cleaned_data['username']:
                request.user.username = form.cleaned_data['username']
            if form.cleaned_data['email']:
                request.user.email = form.cleaned_data['email']
            if form.cleaned_data['password']:
                request.user.set_password(form.cleaned_data['password'])
            if form.cleaned_data.get('first_name'):
                request.user.first_name = form.cleaned_data['first_name']
            if form.cleaned_data.get('last_name'):
                request.user.last_name = form.cleaned_data['last_name']
            if form.cleaned_data['avatar']:
                request.user.avatar = form.cleaned_data['avatar']
            if form.cleaned_data['bio']:
                request.user.bio = form.cleaned_data['bio']
                
            request.user.save()
            return redirect('profilePage')
    else:
        form = UserForm()
    context = {'form': form}
    return render(request, "update-user.html", context)