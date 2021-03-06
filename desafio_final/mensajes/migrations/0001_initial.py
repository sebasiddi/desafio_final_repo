# Generated by Django 4.0.4 on 2022-06-23 23:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_envia', models.IntegerField()),
                ('id_recibe', models.IntegerField()),
                ('titulo_mensaje', models.CharField(max_length=50)),
                ('cuerpo_mensaje', models.CharField(max_length=3000)),
                ('fecha_mesaje', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
