from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('ctl', views.ctl, name='ctl'),
    path('contacts', views.contacts, name='contacts'),
    path('cart', views.cart, name='cart'),
    path('login', views.login, name='login'),
    path('faq', views.faq, name='faq'),
    path('pay', views.pay, name='pay'),
    path('love', views.love, name='favorite'),
]
