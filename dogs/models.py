from django.db import models

NULLABLE = {'blank': True, 'null': True}

class Breed(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    destcription = models.CharField(max_length=500, verbose_name='Описание', **NULLABLE)
    def __str__(self):
        return f'{self.name}'


class Dog(models.Model):
    name = models.CharField(max_length=100, verbose_name='Кличка')
    breed = models.ForeignKey(Breed , on_delete=models.CASCADE, verbose_name='Порода')
    #breed = models.CharField(max_length=100, verbose_name='Порода')
    photo = models.ImageField(upload_to='photo/', verbose_name='Аватар', **NULLABLE)
    birth_day = models.DateField(**NULLABLE, verbose_name='Дата рождения')

    def __str__(self):
        return f'{self.name} {self.breed}'


class Meta:
    verbose_name = 'Порода'
    verbose_name_plural = 'Породы'
