from django.shortcuts import render
from dogs.models import Dog, Breed
from django.views.generic import ListView, DetailView , CreateView
from django.urls import reverse_lazy

def index(request):
    dogs_list = Dog.objects.all()[:3]
    context = {
        "object_list": dogs_list,
        "title": 'Питомник - Главная'
    }
    return render(request, 'dogs/index.html', context)


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
    fields = ('name', 'breed', )
    success_url = reverse_lazy('dogs:dogs_list')
    template_name = 'dogs/dog_from.html'