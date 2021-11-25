from django.shortcuts import render, redirect
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


def createPost(request):

    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/user.html', context)
