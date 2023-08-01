from django.contrib import admin
from dogs.models import Dog, Breed, Parent


# admin.site.register(Dog)

@admin.register(Breed)
class BredAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ('name', 'breed',)
    list_filter = ('breed',)


@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ('name',)
