from django.shortcuts import render
from catalog.models import Product
from django.shortcuts import render, reverse

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy


#def catalog(request):
#    return render(request, 'catalog/contacts.html')


class ContactView(TemplateView):
    template_name = 'catalog/contacts.html'
    extra_context = {"title": 'Контакты'}


class HomeView(ListView):
    model = Product
    template_name = 'catalog/index.html'

"""def home(request):
    product_list = Product.objects.all()
    context = {
        "object_list": product_list,
        "title": 'Товары'
    }

    return render(request, 'catalog/index.html', context)
"""