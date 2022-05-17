from .views import *

from django.urls import path

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

