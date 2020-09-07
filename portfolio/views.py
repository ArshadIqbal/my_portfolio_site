from django.shortcuts import render
import random
# Create your views here.

def homepage(request):
    return render(request, 'portfolio/index.html')
