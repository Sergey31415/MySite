from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def ctl(request):
    return render(request, "main/ctl.html")


def contacts(request):
    return render(request, 'main/contacts.html')


def cart(request):
    return render(request, 'main/cart.html')


def login(request):
    return render(request, 'main/login.html')


def faq(request):
    return render(request, 'main/faq.html')


def pay(request):
    return render(request, 'main/pay.html')


def love(request):
    return render(request, 'main/love.html')