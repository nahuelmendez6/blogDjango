from os import confstr

from django.shortcuts import render, redirect
from blogs.models import Category, Blog
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth.models import Group

def home(request):

    posts = Blog.objects.filter(is_featured=True).order_by('-updated_at')
    context = {
        'featured_post':posts
    }

    return render(request, 'home.html', context)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='blog_group')
            group.user_set.add(user)
            return redirect('register')
    else:
        form = RegistrationForm()

    context = {
        'form':form
    }
    return render(request, 'register.html', context)


def login(request):
    form = AuthenticationForm(request, request.POST)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
            return redirect('home')
    context = {
        'form':form
    }
    return render(request, 'login.html', context)