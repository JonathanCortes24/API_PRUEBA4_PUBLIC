# Generated by Django 3.2.5 on 2021-07-09 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('correo', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=20)),
            ],
        ),
    ]
