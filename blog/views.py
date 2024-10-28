from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Post


# Create your views here.
def home(request):
    
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'title': 'Home'
    }
    return render(request, 'blog/home.html', context)


def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'blog/about.html', context)


@login_required(login_url='login')
def myposts(request):
    user = request.user
    
    if user.is_authenticated:
        posts = Post.objects.filter(author=user.id)
    
    context = {
        'posts': posts,
        'title': 'My Post'
    }
    
    return render(request, 'blog/myposts.html', context)
        
