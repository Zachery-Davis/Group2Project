from django.shortcuts import render

# Create your views here.

def landingPage(request):
    context = {}
    return render(request, "landing.html", context)
