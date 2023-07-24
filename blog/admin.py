from django.contrib import admin
from blog.models import Blog


@admin.register(Blog)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('heading', 'content', 'slug', 'preview', 'is_published')
    list_filter = ('is_published',)
    search_fields = ('heading', 'content', 'date_of_create')
