from django.shortcuts import render
from blogs.models import Category, Blog

def home(request):
    categories = Category.objects.all()
    posts = Blog.objects.filter(is_featured=True).order_by('-updated_at')
    context = {
        'categories': categories,
        'featured_post':posts
    }

    return render(request, 'home.html', context)