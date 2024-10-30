from django.shortcuts import render

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