from django.shortcuts import render
from .models import IndexSlider

def index(request):
    sliders = IndexSlider.objects.all()
    return render(request, 'index/index.html',{'sliders':sliders})
