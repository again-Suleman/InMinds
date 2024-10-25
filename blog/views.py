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