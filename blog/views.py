from django.forms import inlineformset_factory
from django.shortcuts import render
from datetime import date
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
# , TemplateView оставил для других проектов
from pytils.translit import slugify
from django.urls import reverse_lazy, reverse
from blog.models import Blog, Version
from django.shortcuts import get_object_or_404, redirect
from blog.forms import BlogForm, VersionFrom


class BlogCreatView(CreateView):
    model = Blog
    form_class = BlogForm

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
        self.object.save(update_fields=['count_of_views'])
        return self.object


class BlogListView(ListView):
    model = Blog



    def get_queryset(self):
        queryset = super().get_queryset()
        active_versions = Version.objects.filter(is_active=True).select_related('product')
        active_products = {version.product_id: version for version in active_versions}
        for product in queryset:
            product.active_version = active_products.get(product.id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        context['products'] = queryset
        return context



class BlogUpdateView(UpdateView):
    model = Blog
    form_class = BlogForm

    def get_success_url(self):
        return reverse('blog:view', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        BlogFormset = inlineformset_factory(Blog, Version, form=VersionFrom, extra=1)
        if self.request.method == 'POST':
            formset = BlogFormset(self.request.POST, instance=self.object)
        else:
            formset = BlogFormset(instance=self.object)

        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        # with open('file.txt', 'wt', encoding='UTF-8')as file:
        #    file.write(str(context_data))
        formset = context_data['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:start_list')


class FullListView(ListView):
    model = Blog
    template_name = 'blog/blog_full_list.html'
