from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Category, Tag
from .forms import postForm
from django.contrib.auth.decorators import login_required

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


def blogArticle(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'blog/blogarticle.html', {'article': article})


@login_required
def blogNew(request):
    categorys = Category.objects.filter()
    tags = Tag.objects.filter()
    if request.method == 'POST':
        form = postForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            print(post)
            post.author = request.user
            post.save()
            return redirect('blog.views.blogArticle', pk=post.pk)
    else:
        form = postForm()
    return render(request, 'blog/blognew.html', {'form': form, 'categorys': categorys, 'tags': tags})


@login_required
def blogEdit(request, pk):
    categorys = Category.objects.filter()
    tags = Tag.objects.filter()
    post = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = postForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            print(post)
            post.author = request.user
            post.save()
            return redirect('blog.views.blogArticle', pk=post.pk)
    else:
        form = postForm(instance=post)
    return render(request, 'blog/blognew.html', {'form': form, 'categorys': categorys, 'tags': tags})