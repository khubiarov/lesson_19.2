from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.CharField(max_length=300, verbose_name="Описание", **NULLABLE)

    # create_at = models.DateField(verbose_name='date_at', **NULLABLE)
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.CharField(max_length=100, verbose_name='Описание')
    image = models.ImageField(upload_to='photo/', verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="категория")
    price = models.FloatField(verbose_name='Цена')
    date_of_create = models.DateTimeField(verbose_name='Дата создания', **NULLABLE)
    date_of_last_change = models.DateField(verbose_name='Дата последнего изменения', **NULLABLE)

    def __str__(self):
        return self.name
