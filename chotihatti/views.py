from django.shortcuts import render

from .models import Chunris
from .models import Jewellery
from .models import Dresses
from .models import NewArrivals


def home(request):
    arrivals = NewArrivals.objects.all()
    chunris = Chunris.objects.all().order_by('-date_added')[:6]
    dresses = Dresses.objects.all().order_by('-date_added')[:5]
    jewelleries = Jewellery.objects.all().order_by('-date_added')[:5]

    # context dictionary to render all the variables
    context = {'arrivals': arrivals, 'chunris': chunris,
               'dresses': dresses, 'jewelleries': jewelleries}

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
