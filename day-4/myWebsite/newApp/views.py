from django.shortcuts import render, get_object_or_404
from .models import Product 

def app(request):
    products = Product.objects.all()
    return render(request , 'newApp/app.html',{'products': products})
def home(request):
    return render(request, 'website/index.html')

def about(request):
    return render(request, 'website/about.html')

def contact(request):
    return render(request, 'website/contact.html')
def product_details(request,id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'newApp/product_details.html', {'product': product})