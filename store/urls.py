from .views import *

from django.urls import path

urlpatterns = [
    path('', index),
    path('post/<int:post_id>', show_post, name='post')


]

