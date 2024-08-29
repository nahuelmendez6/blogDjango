from unicodedata import category

from django.http import HttpResponse
from django.shortcuts import render
from blogs.models import Blog


# Create your views here.

def posts_by_category(request, category_id):
    posts = Blog.objects.filter(status='Published', category=category_id)
    context = {
        'posts':posts
    }

    return render(request, 'posts_by_category.html', context)