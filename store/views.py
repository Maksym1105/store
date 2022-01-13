from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def index(request):
    posts = Phones.objects.all()
    # context = {
    #     'post': posts,
    # }

    return render(request, 'store/index.html', {'posts': posts})

def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи с id={post_id}')

