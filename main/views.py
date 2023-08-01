from django.forms import inlineformset_factory
from django.shortcuts import render, redirect
from main.models import Student, Subject
from django.shortcuts import get_list_or_404, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from main.forms import StudentFrom, SubjectForm


class StudentListView(ListView):
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
    form_class = StudentFrom
    success_url = reverse_lazy('main:index')


'''class StudentCreateView(CreateView):
    model = Student
    fields = ('first_name', 'last_name', 'avatar')
    success_url = reverse_lazy('main:index')
'''

# урок по формам
'''class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentFrom
    success_url = reverse_lazy('main:index')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        SubjectFormset = inlineformset_factory(Student, Subject, form='SubjectFrom', extra=1)
        context_data['formset'] = SubjectFormset()
        return context_data
'''


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentFrom
    success_url = reverse_lazy('main:index')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        SubjectFormset = inlineformset_factory(Student, Subject, form=SubjectForm, extra=1)
        if self.request.method == 'POST':

            context_data['formset'] = SubjectFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = SubjectFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


'''class StudentUpdateView(UpdateView):
    model = Student
    fields = ('first_name', 'last_name', 'avatar')
    success_url = reverse_lazy('main:index')
'''


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
