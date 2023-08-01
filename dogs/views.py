from django.forms import inlineformset_factory
from django.shortcuts import render, reverse

from dogs.froms import DogForm, ParentForm
from dogs.models import Dog, Breed, Parent
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy

"""def index(request):
    dogs_list = Dog.objects.all()[:3]
    context = {
        "object_list": dogs_list,
        "title": 'Питомник - Главная'
    }
    return render(request, 'dogs/index.html', context)
"""


class IndexView(TemplateView):
    template_name = 'dogs/index.html'
    extra_context = {

        "title": 'Питомник - Главная'
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Breed.objects.all()[:3]
        return context_data


"""def breeds(request):
    dogs_list = Dog.objects.all()
    context = {
        "object_list": dogs_list,
        "title": 'Все наши породы'
    }
    return render(request, 'dogs/breeds.html', context)
"""


class Breeds(ListView):
    model = Breed
    template_name = 'dogs/breeds.html'
    extra_context = context = {

        "title": 'Все наши породы'
    }


'''def breeds_dogs(request, pk):
    breed_item = Breed.objects.get(pk=pk)
    context = {
        "object_list": Dog.objects.filter(breed_id=pk),
        "title": f'Собаки породы {breed_item.name}'
    }
    return render(request, 'dogs/dogs.html', context)
    '''


class DogsListView(ListView):
    model = Dog
    template_name = 'dogs/dogs.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(breed_id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        breed_item = Breed.objects.get(pk=self.kwargs.get('pk'))
        context_data['breed_id'] = breed_item.pk,
        context_data['title'] = f'Собаки породы {breed_item.name}'

        return context_data


class DogCreateView(CreateView):
    model = Dog

    form_class = DogForm
    success_url = reverse_lazy('dogs:breeds')


class DogUpdateView(UpdateView):
    model = Dog

    form_class = DogForm

    def get_success_url(self):
        return  reverse('dogs:dog_update',  args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ParentFormset = inlineformset_factory(Dog, Parent, form=ParentForm, extra=1)
        if self.request.method == 'POST':
            formset = ParentFormset(self.request.POST, instance=self.object)
        else:
            formset = ParentFormset(instance=self.object)

        context_data['formset'] = formset
        # with open('file', 'wt', encoding='UTF-8') as file:
        #    file.write(str(context_data))
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


class DogDeleteView(DeleteView):
    model = Dog
    success_url = reverse_lazy('dogs:breeds')
