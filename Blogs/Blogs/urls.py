"""Blogs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Ayush),
    path('Django.html', views.django, name='Django'),
    path('DjangoRs.html', views.djangorest, name='DjangoRs'),
    path('contact.html', views.cont, name='contact'),
    path('interview.html', views.Inv, name='interview'),
    path('signup.html', views.Sign, name='signup'),
    path('login.html', views.log, name='login'),


]
