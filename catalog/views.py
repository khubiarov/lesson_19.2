from django.shortcuts import render


# Create your views here.

def catalog(request):
    return render(request, 'catalog/contacts.html')


def home(request):
    return render(request, 'catalog/home.html')


