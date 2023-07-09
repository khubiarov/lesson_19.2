from django.shortcuts import render
from dogs.models import Dog, Breed


def index(request):
    dogs_list = Dog.objects.all()[:3]
    context = {
        "object_list": dogs_list,
        "title": 'Питомник - Главная'
    }
    return render(request, 'dogs/index.html', context)


def breeds(request):
    dogs_list = Dog.objects.all()
    context = {
        "object_list": dogs_list,
        "title": 'Все наши породы'
    }
    return render(request, 'dogs/breeds.html', context)


def breeds_dogs(request, pk):
    breed_item = Breed.objects.get(pk=pk)
    context = {
        "object_list": Dog.objects.filter(breed_id=pk),
        "title": f'Собаки породы {breed_item.name}'
    }
    return render(request, 'dogs/dogs.html', context)