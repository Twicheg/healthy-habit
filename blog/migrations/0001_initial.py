# Generated by Django 4.2.4 on 2023-09-24 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publication_date', models.DateTimeField(auto_created=True, blank=True, null=True, verbose_name='дата публикации')),
                ('title', models.CharField(max_length=50, verbose_name='заголовок')),
                ('text_body', models.TextField(verbose_name='содержание статьт')),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog/', verbose_name='изображение')),
                ('number_of_views', models.IntegerField(blank=True, null=True, verbose_name='количество просмотров')),
            ],
            options={
                'verbose_name': 'Блог',
                'verbose_name_plural': 'Блоги',
            },
        ),
    ]
