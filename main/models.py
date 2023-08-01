from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Student(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='имя')
    last_name = models.CharField(max_length=100, verbose_name='фамилия')
    avatar = models.ImageField(upload_to='students/', verbose_name='аватар', **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name="Учится")
    email = models.CharField(max_length=150, verbose_name='email' ,unique=True, **NULLABLE)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"
        ordering = ('last_name',)


class Subject(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Описание' )

    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Студент')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'




