from django.urls import path

from main.views import StudentListview, contact, StudentDetailView, StudentCreateView, StudentUpdateView, \
    StudentDeleteView, toggle_activity
from main.apps import MainConfig

app_name = MainConfig.name

urlpatterns = [

    path('', StudentListview.as_view(), name='index'),
    path('contact/', contact, name='contact'),
    path('<int:pk>/view/', StudentDetailView.as_view(), name='view_student'),
    path('create/', StudentCreateView.as_view(), name='create_student'),
    path('<int:pk>/edit/', StudentUpdateView.as_view(), name='update_student'),
    path('<int:pk>/delete/', StudentDeleteView.as_view(), name='delete_student'),
    path('<int:pk>/activity/', toggle_activity, name='toggle_activity'),


]
