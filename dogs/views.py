from django.shortcuts import render, reverse
from dogs.models import Dog, Breed
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
    fields = ('name', 'breed',)
    success_url = reverse_lazy('dogs:index')
    template_name = 'dogs/dog_from.html'


class DogUpdateView(UpdateView):
    model = Dog
    fields = ('name', 'breed',)
    # success_url = reverse_lazy('dogs:index')
    template_name = 'dogs/dog_from.html'

    def get_success_url(self):
        return reverse('dogs:dogs_list', args=[self.object.breed.pk])


class DogDeleteView(DeleteView):
    model = Dog
    success_url = reverse_lazy('dogs:breeds')
