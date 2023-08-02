"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# from catalog.views import catalog, home

urlpatterns = [
                  path('admin/', admin.site.urls),
                  # path('home/', include('catalog.urls')),
                  path('', include('catalog.urls')),
                  path('dogs/', include('dogs.urls', namespace='dogs')),
                  path('lesson20_2/', include('lesson_20_2.urls')),
                  path('main/', include('main.urls', namespace='main')),
                  path('materials/', include('materials.urls', namespace='materials')),
                  path('blog/', include('blog.urls', namespace='blog'))

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
