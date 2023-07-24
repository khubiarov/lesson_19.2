from django.shortcuts import render
from datetime import date
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView, DetailView

from pytils.translit import slugify
from django.urls import reverse_lazy, reverse
from blog.models import Blog


class BlogCreatView(CreateView):
    model = Blog

    fields = ('heading', 'content', 'preview',)
    success_url = reverse_lazy('blog:start_list')  # Здесь вроде переделать

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.date_of_create = date.today()
        self.object.save()
        return self.object


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_of_views += 1
        self.object.save()
        return self.object


class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('heading', 'content', 'preview',)
    success_url = reverse_lazy('blog:view')# Не работает

class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:start_list')