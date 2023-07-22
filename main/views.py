from django.shortcuts import render, redirect
from main.models import Student
from django.shortcuts import get_list_or_404, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse


class StudentListview(ListView):
    model = Student
    template_name = 'main/student_list.html'


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


class StudentDetailView(DetailView):
    model = Student


class StudentCreateView(CreateView):
    model = Student
    fields = ('first_name', 'last_name', 'avatar')
    success_url = reverse_lazy('main:index')


class StudentUpdateView(UpdateView):
    model = Student
    fields = ('first_name', 'last_name', 'avatar')
    success_url = reverse_lazy('main:index')


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('main:index')


def toggle_activity(request, pk):
    student_item = get_object_or_404(Student, pk=pk)
    if student_item.is_active:
        student_item.is_active = False

    else:
        student_item.is_active = True

    student_item.save()

    return redirect(reverse('main:index'))
