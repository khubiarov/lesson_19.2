from django.shortcuts import render
from datetime import date
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
#, TemplateView оставил для других проектов
from pytils.translit import slugify
from django.urls import reverse_lazy, reverse
from blog.models import Blog
from django.shortcuts import get_object_or_404, redirect


class BlogCreatView(CreateView):
    model = Blog

    fields = ('heading', 'content', 'preview')
    success_url = reverse_lazy('blog:start_list')
    extra_context = {

        "title": 'Создание публикации'
    }

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.heading)
            new_blog.date_of_create = date.today()
            new_blog.save()

        return super().form_valid(form)


def published_func(request, pk):
    student_item = get_object_or_404(Blog, pk=pk)
    if student_item.is_published:
        student_item.is_published = False

    else:
        student_item.is_published = True

    student_item.save()

    return redirect(reverse('blog:full_list'))


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
    fields = ('heading', 'content', 'preview')

    def get_success_url(self):
        return reverse('blog:view', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:start_list')

class FullListView(ListView):
    model = Blog
    template_name = 'blog/blog_full_list.html'
