"""
URL configuration for SkillSync project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.landingPage, name="landingPage"),
    
    path("register/", views.registerPage, name="registerPage"),
    path("login/", views.loginPage, name="loginPage"),
    path("logout/", views.logoutUser, name="logout"),
    path("profile/<str:user>/", views.profilePage, name="profilePage"),
    path("updateUser/", views.updateUserPage, name="updateUser"),
    
    path("dashboard/", views.dashboardPage, name="dashboardPage"),

    path("<str:user>/tree/<str:name>", views.treePage, name="treePage"),
    path("toggleLeaf/<str:treeName>/<str:nodeName>/", views.toggleLeaf, name="toggleLeaf"),
    path("createTree/", views.createTreePage, name="createTree"),
    path("togglePublicTree/<str:name>", views.togglePublicTree, name="togglePublicTree"),
    path("deleteTree/<str:name>", views.deleteTree, name="deleteTree"),
]