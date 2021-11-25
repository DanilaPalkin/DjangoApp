from django.shortcuts import render
from .models import *


def feed(request):
    posts = Post.objects.all()
    return render(request, 'accounts/dashboard.html', {'posts': posts})


def post(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'accounts/posts.html', {'post': post})


def user(request, pk):
    posts = Post.objects.filter(author=pk)
    return render(request, 'accounts/dashboard.html', {'posts': posts})
