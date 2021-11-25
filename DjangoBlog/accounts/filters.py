import django_filters
from django_filters import CharFilter
from django.db.models import Q
from .models import *


class PostFilter(django_filters.FilterSet):
    search = CharFilter(method='multipleFilter')

    class Meta:
        model = Post
        fields = ['search']

# https://stackoverflow.com/questions/57270470/django-filter-how-to-make-multiple-fields-search-with-django-filter
    def multipleFilter(self, queryset, name, value):
        return Post.objects.filter(
            Q(title__icontains=value) | Q(text__icontains=value)
        )
