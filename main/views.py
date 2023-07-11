from django.shortcuts import render
from main.models import  Student


def main(request):
    students_list = Student.objects.all()

    context = {
        'object_list': students_list
    }

    return render(request, 'main/index.html', context)
