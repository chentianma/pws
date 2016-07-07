from django.shortcuts import render
from .models import Article, Category, Tag

# Create your views here.


def blogHome(request):
    articles = Article.objects.filter(publish_date__isnull=False).order_by('-created_date')
    print(articles)
    return render(request, 'blog/bloghome.html', {'articles': articles})