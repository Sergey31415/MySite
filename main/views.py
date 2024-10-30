from django.shortcuts import render, get_object_or_404, redirect

from main.cart import Cart
from main.models import Product, Answers_and_Questions


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def ctl(request):
    products = Product.objects.all()
    return render(request, "main/ctl.html", {'products': products})


def contacts(request):
    return render(request, 'main/contacts.html')


def cart(request):
    return render(request, 'main/cart.html')


def login(request):
    return render(request, 'main/login.html')


def faq(request):
    faqs = Answers_and_Questions.objects.all()
    return render(request, 'main/faq.html', {'faqs': faqs})


def pay(request):
    return render(request, 'main/pay.html')


def love(request):
    return render(request, 'main/love.html')


def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product, quantity=1)  # по умолчанию добавляем 1 товар
    return redirect('cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'main/cart.html', {'cart': cart})
