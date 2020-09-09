from django.shortcuts import render
from .models import IndexSlider
from .models import Navigation_brand
from .models import Address




def index(request):
    sliders = IndexSlider.objects.all()
    adresses = Address.objects.all()
    
    return render(request, 'index/index.html',{'sliders':sliders, 'adresses':adresses})




