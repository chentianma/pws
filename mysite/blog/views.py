from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Category, Tag
from .forms import postForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def blogHome(request):
    articles = Article.objects.filter(publish_date__isnull=False).order_by('-publish_date')
    return render(request, 'blog/bloghome.html', {'articles': articles})


def blogIndex(request):
    categorys = Category.objects.all()
    article = Article.objects.filter(publish_date__isnull=False)
    return render(request, 'blog/blogindex.html', {'categorys': categorys, 'article': article})


def blogAbout(request):
    return render(request, 'blog/blogabout.html')


def blogMessage(request):
    return render(request, 'blog/blogmessage.html')


def blogArticle(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.click += 1
    article.save()
    # print('{0}(click_number):{1}'.format(article.title, article.click))
    return render(request, 'blog/blogarticle.html', {'article': article})


@login_required
def blogNew(request):
    if request.method == 'POST':
        form = postForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            re_get = Article.objects.get(id=post.pk)
            re_get.publish()
            print(re_get.title)
            return redirect('article', pk=post.pk)
    else:
        form = postForm()
    return render(request, 'blog/blognew.html', {'form': form})


@login_required
def blogEdit(request, pk):
    post = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = postForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            print(post)
            post.author = request.user
            post.save()
            return redirect('article', pk=post.pk)
    else:
        form = postForm(instance=post)
    return render(request, 'blog/blognew.html', {'form': form})