from django.contrib.auth import admin

from .views import *

from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='home'),
    path('post/<int:post_id>', show_post, name='post'),
    path('brand/Apple', show_brand_iphone, name='iphone_page'),
    path('brand/Samsung', show_brand_samsung, name='samsung_page'),
    path('brand/Xiaomi', show_brand_xiaomi, name='xiaomi_page'),
    path('login', LoginUser.as_view(), name='login_page'),
    path('register', RegisterUser.as_view(), name='registration_page'),
    path('logout', LogoutUser, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
