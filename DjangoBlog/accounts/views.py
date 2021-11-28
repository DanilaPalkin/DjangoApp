from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import *
from .forms import PostForm
from .filters import PostFilter


def feed(request):
    posts = Post.objects.all()
    myFilter = PostFilter(request.GET, queryset=posts)
    posts = myFilter.qs
    context = {'posts': posts, 'myFilter': myFilter}
    return render(request, 'accounts/dashboard.html', context)


def post(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'accounts/posts.html', {'post': post})


def user(request, pk):
    posts = Post.objects.filter(author=pk)
    return render(request, 'accounts/dashboard.html', {'posts': posts})


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы были успешно зарегистрированы!')
            return redirect('/login')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Неправильный логин или пароль')
    context = {}
    return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('/login')


def createPost(request):
    if request.user.is_anonymous:
        return redirect('/')
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.author = request.user
            newpost.save()
            return redirect('/')
    else:
        form = PostForm()
    return render(request, 'accounts/user.html', {'form': form})

def deletePost(request, pk):
    if request.user.is_anonymous:
        return redirect('/')
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('/')
    return render(request, 'accounts/delete.html', {'post': post})
