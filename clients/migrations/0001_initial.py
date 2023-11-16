# Generated by Django 4.2.4 on 2023-09-26 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=150, verbose_name='емейл')),
                ('first_name', models.CharField(max_length=100, verbose_name='имя')),
                ('last_name', models.CharField(max_length=100, verbose_name='фамилия')),
                ('surname', models.CharField(max_length=100, verbose_name='отчество')),
                ('comments', models.TextField(verbose_name='комментарии')),
                ('content_creator', models.EmailField(blank=True, max_length=50, null=True, verbose_name='создатель клиента')),
            ],
            options={
                'verbose_name': 'клиент',
                'verbose_name_plural': 'клиенты',
            },
        ),
    ]
