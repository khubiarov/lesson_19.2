from django.urls import path

from dogs.apps import DogsConfig
from dogs.views import   Breeds, DogsListView, DogCreateView, DogUpdateView, DogDeleteView, IndexView
#index,

app_name = DogsConfig.name

urlpatterns = [

    path('', IndexView.as_view(), name='index'),
    path('breeds/', Breeds.as_view(), name='breeds'),
    path('<int:pk>/dogs/', DogsListView.as_view(), name='dogs_list'),
    path('create/', DogCreateView.as_view(), name='dog_create'),
    path('<int:pk>/edit/', DogUpdateView.as_view(), name='dog_update'),
    path('<int:pk>/delete/', DogDeleteView.as_view(), name='dog_delete')

]
