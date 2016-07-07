from django.shortcuts import render
from .models import Article, Category, Tag

# Create your views here.


def blogHome(request):
    articles = Article.objects.filter(publish_date__isnull=False).order_by('-created_date')
    return render(request, 'blog/bloghome.html', {'articles': articles})


def blogIndex(request):
    return render(request, 'blog/blogindex.html')


def blogAbout(request):
    return render(request, 'blog/blogabout.html')


def blogMessage(request):
    return render(request, 'blog/blogmessage.html')