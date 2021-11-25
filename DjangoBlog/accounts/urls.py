from django.urls import path
from . import views

urlpatterns = [
    path('', views.feed),
    path('user/<str:pk>/', views.user),
    path('post/<str:pk>/', views.post),
]