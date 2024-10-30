from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


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
    path('cart/add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart/', views.cart_detail, name='cart_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
