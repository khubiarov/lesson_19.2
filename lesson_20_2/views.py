from django.shortcuts import render


def home_ctrl(request):
    return render(request, 'lesson_20_2/home.html')


def contact_ctrl(request):
    return render(request,'lesson_20_2/contacts.html')


