from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
    heading = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.CharField(max_length=150, verbose_name='slug')
    content = models.TextField(verbose_name='Содержимое', **NULLABLE)
    preview = models.ImageField(upload_to='photo/', verbose_name='Изображение', **NULLABLE)
    date_of_create = models.DateField(verbose_name='Дата создания', **NULLABLE)
    is_published = models.BooleanField(verbose_name='Опубликовано', default=True)
    count_of_views = models.IntegerField(verbose_name='Количество просмотров',default=0)

    def __str__(self):
        return f'{self.heading} {self.date_of_create}'

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = ('date_of_create',)
