# Generated by Django 4.2.5 on 2023-11-24 17:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='название образовательного модуля')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='educational-modules/modules/photo', verbose_name='фото')),
                ('video', models.FileField(blank=True, null=True, upload_to='educational-modules/modules/video', verbose_name='видео')),
                ('count_views', models.PositiveIntegerField(default=0, verbose_name='кол-во просмотров')),
                ('id_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='categories.category', verbose_name='категория')),
                ('id_users', models.ManyToManyField(blank=True, null=True, related_name='id_users', to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'образовательный модуль',
                'verbose_name_plural': 'образовательные модули',
            },
        ),
    ]
    