from django.shortcuts import render, redirect
from .form import MyUserCreationForm
from django.contrib.auth import login
from django.contrib import messages


# Starting Page Of Application
def landingPage(request):
    context = {}
    return render(request, "landing.html", context)

def registerPage(request):
    form = MyUserCreationForm()
    if request.method == "POST":
        form = MyUserCreationForm(request.POST)
        if(form.is_valid()):
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect("landingPage") # Will Be Home When Built
        else:
            messages.error(request, "Registration Has Failed!")
    context = {"form": form}
    return render(request, "register.html", context)
