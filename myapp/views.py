from django.shortcuts import render
from .models import Products
from django.shortcuts import get_object_or_404

def home(request):
  return render(request, 'pages/home.html')

def products_list(request):
  products = Products.objects.all()
  return render(request, 'products/index.html', {'products': products})

def product_detail(request, id):
  product = get_object_or_404(Products, id=id)
  return render(request, 'products/show.html', {'product': product})