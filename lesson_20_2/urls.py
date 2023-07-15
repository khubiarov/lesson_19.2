from django.urls import path

from lesson_20_2.views import home_ctrl, contact_ctrl

app_name = 'lesson_20_2'


urlpatterns =[

    path('', home_ctrl, name='lesson_20_2'),
    path('contacts/', contact_ctrl, name='lesson_20_2')


]