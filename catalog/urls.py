from django.urls import path

from catalog.views import ContactView, HomeView

app_name = 'catalog'

urlpatterns = [
    path('contacts/', ContactView.as_view(), name='catalog'),
    path('', HomeView.as_view(), name='home'),

]
