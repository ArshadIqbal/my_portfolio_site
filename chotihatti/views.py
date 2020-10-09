from django.shortcuts import render
from .models import NewArrivals


def home(request):
    arrivals = NewArrivals.objects.all()
    context = {'arrivals': arrivals}

    return render(request, 'chotihatti/chotihatti.html',  context)


def store(request):
    context = {}
    return render(request, 'chotihatti/store.html', context)


def single_product(request):
    context = {}
    return render(request, 'chotihatti/single-product.html', context)


def cart(request):
    context = {}
    return render(request, 'chotihatti/cart.html', context)


def coming(request):
    context = {}
    return render(request, 'chotihatti/coming_soon.html', context)
