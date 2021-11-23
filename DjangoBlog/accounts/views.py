from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def feed(request):
    posts = Post.objects.all()
    return render(request, 'accounts/dashboard.html', {'posts': posts})


def post(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'accounts/posts.html', {'post': post})


def user(request):
    return render(request, 'accounts/user.html')
