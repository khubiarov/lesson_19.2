from django.shortcuts import render
from main.models import Student
from django.shortcuts import get_list_or_404, get_object_or_404


def main(request):
    students_list = Student.objects.all()

    context = {
        'object_list': students_list,
        'title': "Главная"
    }

    return render(request, 'main/index.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} ({email}): {message}')

    context = {
        'title': 'Контакты'
    }
    return render(request, 'main/contact.html', context)


def view_students(request, pk):
    student_item = get_object_or_404(Student, pk=pk)

    context = {'object': student_item
               }
    return render(request, 'main/student_detail.html', context)
