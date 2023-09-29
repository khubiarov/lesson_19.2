from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from config import settings
from users.froms import UserRegistrationForm, UserProfileForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    success_url = '/'

    def form_valid(self, form):
        new_user = form.save()
        send_mail(subject='Регистрация', message='Вы зарегистрировались', from_email=settings.EMAIL_HOST_USER,
                  recipient_list=[new_user.email]

                  )
        return super().form_valid(form)


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user
