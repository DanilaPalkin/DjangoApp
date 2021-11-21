from django.shortcuts import render
from django.http import HttpResponse


def feed(request):
    return render(request, 'accounts/dashboard.html')


def posts(request):
    return render(request, 'accounts/posts.html')


def user(request):
    return render(request, 'accounts/user.html')
