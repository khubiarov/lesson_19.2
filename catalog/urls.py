from django.urls import path

from catalog.views import catalog, home

app_name = 'catalog'


urlpatterns =[
    path('contacts/', catalog, name='catalog'),
    path('', home, name='home')


]
