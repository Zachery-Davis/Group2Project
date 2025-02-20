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
from api.GrammarGinger import GrammarGinger

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
            messages.success(request, "Login Successful!")
            return redirect("dashboardPage")
        else:
            messages.error(request, "Login failed. Ensure your credentials are correct and try again.")
    else:
        form = AuthenticationForm()
    context = {"page": "login"}
    return render(request, "login_register.html", context)

@login_required(login_url="login")
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

# View Tree Page 
def treePage(request, user, name):
    user = User.objects.get(username=user)
    tree = user.json_data.filter(name=name).first()
    if tree:
        if not tree.public and request.user != user:
            return redirect("dashboardPage")
        jsonData = tree.data
        context = {"jsonData": jsonData, "user": user}
        return render(request, "tree.html", context)
    
    return redirect("dashboardPage")

# Create Tree Page
@login_required(login_url="login")
def createTreePage(request, rerunSubject=None):
    if request.method == "POST" or rerunSubject != None:
        form = TreeForm(request.POST)
        if form.is_valid() or rerunSubject != None:
            if(rerunSubject == None):  
                subject = form.cleaned_data["subject"]
            else:
                subject = rerunSubject
            wordAPI = GrammarGinger(subject)
            wordAPI.analyzeWords()
            if(wordAPI.foundMistake == True):
                messages.error(request, f"Input not recognized. Did you mean '{wordAPI.rebuildPrompt()}'? Please try again.")
                return redirect("createTree")
            api = ChatGPTAPI(apiKey, subject)
            title = api.titleOfTree(api.jsonData)
            description = api.descriptionOfTree(api.jsonData)
            if(title == -1 or description == -1):
                createTreePage(request, subject)
            newTree = UserJsonData(user=request.user, name=title, description=description, data=api.jsonData)
            newTree.save()
            messages.success(request, f"The '{subject}' tree has been successfully constructed.")
            return redirect("dashboardPage")
    context = {}
    return render(request, "tree_form.html", context)

# Delete Tree
@login_required(login_url="login")
def togglePublicTree(request, name):
    user = request.user
    tree = user.json_data.filter(name=name).first()
    if tree:
        tree.public = not tree.public
        tree.save()
    return redirect(request.META.get('HTTP_REFERER'))

# Delete Tree
@login_required(login_url="login")
def deleteTree(request, name):
    user = request.user
    tree = user.json_data.filter(name=name).first()
    if tree:
        tree.delete()
    return redirect("dashboardPage")

# Change Leaf State
@login_required(login_url="login")
def toggleLeaf(request, treeName, nodeName):
    user = request.user

    # Fetch the JSON data for the specified tree name
    jsonDataObj = user.json_data.filter(name=treeName).first()
    if not jsonDataObj:
        messages.error(request, f"Tree '{treeName}' not found.")
        return redirect("dashboardPage")

    # Get the JSON data
    jsonData = jsonDataObj.data

    # Recursive function to find and toggle the node's `completedTask`
    def find_and_toggle(node, target_name, parent_completed=True):
        if node.get("title") == target_name:
            # Check if all subnodes are completed
            for key, child in node.get("extend", {}).items():
                if not child.get("completedTask") == "true":
                    messages.error(request, f"Subnodes of '{nodeName}' are not completed.")
                    return False

            # Toggle the node's `completedTask` based on parent's state
            if parent_completed:
                messages.error(request, f"Parent node of '{nodeName}' is completed.")
                return False
            else:
                node["completedTask"] = "false" if node.get("completedTask") == "true" else "true"
                return True

        # Recursively search in the `extend` field
        for key, child in node.get("extend", {}).items():
            if find_and_toggle(child, target_name, node.get("completedTask") == "true"):
                return True

        return False

    # Find and toggle the node
    node_found = find_and_toggle(jsonData, nodeName)

    if node_found:
        # Save the updated JSON data back to the database
        jsonDataObj.data = jsonData
        jsonDataObj.save()
        messages.success(request, f"Database updated successfully.")

    # Reload tree
    return redirect("treePage", user.username, treeName)

# Profile Page 
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
            return redirect('profilePage', request.user.username)
    else:
        form = UserForm()
    context = {'form': form}
    return render(request, "update-user.html", context)