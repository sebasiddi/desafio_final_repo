# Generated by Django 4.0.4 on 2022-06-24 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mensajes', '0002_remove_mensaje_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mensaje',
            old_name='fecha_mesaje',
            new_name='fecha_mensaje',
        ),
    ]
