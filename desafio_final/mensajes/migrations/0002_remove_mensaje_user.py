# Generated by Django 4.0.4 on 2022-06-24 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mensajes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mensaje',
            name='user',
        ),
    ]
