from django.urls import path

from main.views import main, contact
from main.apps import MainConfig

app_name = MainConfig.name


urlpatterns =[

    path('', main, name='index'),
    path('contact/', contact,name='contact')


]