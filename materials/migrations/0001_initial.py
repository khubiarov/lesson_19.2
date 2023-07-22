# Generated by Django 4.0.4 on 2023-07-15 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название')),
                ('body', models.TextField(verbose_name='Содержимое')),
            ],
            options={
                'verbose_name': 'Материал',
                'verbose_name_plural': 'Материалы',
            },
        ),
    ]
