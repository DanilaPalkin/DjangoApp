from django.urls import path
from . import views

urlpatterns = [
    path('', views.feed),
    path('posts/', views.posts),
    path('user/', views.user),
]