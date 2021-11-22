from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=200, null=True)
    text = models.TextField(null=True, blank=True)
    media = models.ImageField(null=True, blank=True)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['-date_created', ]

    def __str__(self):
        return self.title
