# Generated by Django 4.2.4 on 2023-09-23 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_messagesettings_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagesettings',
            name='message_counter',
            field=models.IntegerField(default=0, verbose_name='счетчик'),
        ),
    ]