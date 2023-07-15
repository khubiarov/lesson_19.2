from django.urls import path

from main.views import main, contact, view_students
from main.apps import MainConfig

app_name = MainConfig.name

urlpatterns = [

    path('', main, name='index'),
    path('contact/', contact, name='contact'),
    path('<int:pk>/view/', view_students, name='view_student')

]
