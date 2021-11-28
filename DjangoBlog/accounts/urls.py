from django.urls import path
from . import views

urlpatterns = [
    path('', views.feed),
    path('user/<str:pk>/', views.user),
    path('post/<str:pk>/', views.post),

    path('register/', views.registerPage),
    path('login/', views.loginPage),
    path('logout/', views.logoutUser),

    path('create_post/', views.createPost),
    path('delete_post/<str:pk>/', views.deletePost),
]