from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200, null=True)
    text = models.TextField(null=True)
    media = models.ImageField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title
