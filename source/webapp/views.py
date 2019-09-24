from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Product, CATEGORY_CHOICES

def index_view(request, *args, **kwargs):
    products = Product.objects.filter(balance__gt=0).order_by('name').order_by('category')
    return render(request, 'index.html', context={
        'products': products
    })

def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product.html', context={
        'product': product
    })