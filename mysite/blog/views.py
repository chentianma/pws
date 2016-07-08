from django.shortcuts import render, get_object_or_404
from .models import Article, Category, Tag

# Create your views here.


def blogHome(request):
    articles = Article.objects.filter(publish_date__isnull=False).order_by('-created_date')
    for a in articles:
        print(a.id)
    return render(request, 'blog/bloghome.html', {'articles': articles})


def blogIndex(request):
    return render(request, 'blog/blogindex.html')


def blogAbout(request):
    return render(request, 'blog/blogabout.html')


def blogMessage(request):
    return render(request, 'blog/blogmessage.html')


def blogArticle(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'blog/blogarticle.html', {'article': article})