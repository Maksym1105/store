from django.contrib.auth import logout
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView


from .forms import RegisterUserForm, LoginUserForm
from .models import *


def index(request):
    posts = Phones.objects.all()

    return render(request, 'store/index.html', {'posts': posts})


def show_post(request, post_id):
    post = get_object_or_404(Phones, pk=post_id)

    context = {
        'post': post,
        'title': post.title,
        'brand': post.brand,
        'price': post.price,
    }

    return render(request, 'store/post.html', context=context)


def show_brand_iphone(request):
    posts_apple = Phones.objects.filter(brand_id='1')

    context = {
        'posts': posts_apple,
    }

    return render(request, 'store/iphone.html', context=context)


def show_brand_samsung(request):
    posts_samsung = Phones.objects.filter(brand_id='3')

    context = {
        'posts': posts_samsung,
    }

    return render(request, 'store/samsung.html', context=context)


def show_brand_xiaomi(request):
    posts_xiaomi = Phones.objects.filter(brand_id='2')

    context = {
        'posts': posts_xiaomi,
    }

    return render(request, 'store/xiaomi.html', context=context)

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'store/login.html'

    def get_success_url(self):
        return reverse_lazy('home')

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'store/register.html'
    success_url = reverse_lazy('login_page')

    def form_valid(self, form):
        form.save
        return super(RegisterUser, self).form_valid(form)

def LogoutUser(request):
    logout(request)
    return redirect('login_page')

