from django.shortcuts import render
from .models import Article
# from django.http import HttpResponse

# Create your views here.
def home_page(requests):
    articles = Article.objects.all
    context = {'articles': articles}
    return render(requests, 'home_page.html', context)


def article_page(requests, slug):
    article = Article.objects.get(slug=slug)
    context = {'article': article}
    return render(requests, 'article_page.html', context)
