from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(requests):
    return HttpResponse('''<html>
    <title>Сайт Айнара Ерошенкова</title>
    <h1>Айнар Ерошенков</h1>
    </html>''')
