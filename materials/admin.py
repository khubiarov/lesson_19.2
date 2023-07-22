from django.contrib import admin
from materials.models import Material

@admin.register(Material)
class BredAdmin(admin.ModelAdmin):
    list_display = ('title','body', )
