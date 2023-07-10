from django.shortcuts import render
from catalog.models import Product

# Create your views here.

def catalog(request):
    return render(request, 'catalog/contacts.html')


def home(request):
    product_list = Product.objects.all()
    context = {
        "object_list": product_list,
        "title": 'Товары'
    }

    return render(request, 'catalog/index.html', context)


