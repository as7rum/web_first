from django.shortcuts import render
from .models import Article
# from django.http import HttpResponse

# Create your views here.
def home_page(requests):
    articles = Article.objects.all
    context = {'articles': articles}
    return render(requests, 'home_page.html', context)
    
    # return HttpResponse('''<html>
    # <title>Сайт Айнара Ерошенкова</title>
    # <h1>Айнар Ерошенков</h1>
    # </html>''')
