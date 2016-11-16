from django.shortcuts import render
from datetime import datetime

from .models import Post

def index(request):
    return render(request, 'index.html', context={'who': 'IU5'})


def feed(request):
    # Достаем данные из БД

    posts = Post.objects.all()

    return render(request, 'feed.html', context={'posts': posts})
