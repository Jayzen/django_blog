from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Article
from .forms import ArticleForm, RegisterForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, 'article/home.html', {})


def articles(request):
    articles = Article.objects.all()
    return render(request, "article/articles.html", {"articles": articles})


def article(request, pk):
    article = Article.objects.get(id=pk)
    return render(request, "article/article.html", {"article": article})


@login_required(login_url="/login")
def article_delete(request, pk):
    article = Article.objects.filter(id=pk).first()
    if article.user == request.user:
        article = Article.objects.get(id=pk)
        article.delete()
        return redirect("articles")
    else:
        return redirect("articles")


@login_required(login_url="/login")
def article_new(request):

    if request.method == "POST":
        form = ArticleForm(request.POST)
        print(form)

        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            user = request.user
            article = Article(title=title, content=content, user=user)
            article.save()
        return redirect("articles")

    else:
        form = ArticleForm()

    return render(request, "article/new.html", {"form": form})


@login_required(login_url="/login")
def article_edit(request, pk):
    article = Article.objects.filter(id=pk).first()
    if article.user == request.user:
        if request.method == "POST":

            form = ArticleForm(request.POST)
            print(form)
            Article.objects.filter(id=pk).update(
                title=form.cleaned_data["title"],
                content=form.cleaned_data["content"]
            )
            return redirect("articles")
        else:
            article = Article.objects.get(id=pk)
            article = ArticleForm({"title": article.title, "content": article.content})
            return render(request, "article/edit.html", {"article": article, "id": pk})
    else:
        return redirect("articles")


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {"form": form})


