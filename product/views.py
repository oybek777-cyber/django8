from django.shortcuts import render
from .models import Product
# Create your views here.

def product(request):
    product=Product.objects.all()
    # print('------->',product)
    context={
        'product':product
    }

    return render(request, 'home.html',context=context)

def detail_product(request,id):  
    product=Product.objects.get(id=id)
    context={
        'product':product
    }
    return render(request, 'detail.html' ,context=context)