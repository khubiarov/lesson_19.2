from django.contrib import admin
from main.models import Student,Subject


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'avatar', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('first_name', 'last_name')

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'student')
    list_filter = ('student',)