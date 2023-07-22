from django.urls import path

from dogs.apps import DogsConfig
from dogs.views import index,  Breeds, DogsListView, DogCreateView

app_name = DogsConfig.name

urlpatterns = [

    path('', index, name='index'),
    path('breeds/', Breeds.as_view(), name='breeds'),
    path('<int:pk>/dogs/', DogsListView.as_view(), name='dogs_list'),
    path('create/', DogCreateView.as_view(), name='dog_create')
]
