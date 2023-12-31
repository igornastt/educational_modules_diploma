# Generated by Django 4.2.6 on 2023-11-24 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='название')),
                ('description', models.TextField(verbose_name='описание')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='educational-modules/categories/photo', verbose_name='фото')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
            },
        ),
    ]
