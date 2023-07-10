from django.contrib import admin
from main.models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'avatar', 'is_active')
    #list_filter = ('category',)
    #search_fields = ('name', 'description')

