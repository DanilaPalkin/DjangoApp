from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def feed(request):
    posts = Post.objects.all()
    return render(request, 'accounts/dashboard.html', {'posts': posts})


def posts(request):
    return render(request, 'accounts/posts.html')


def user(request):
    return render(request, 'accounts/user.html')
