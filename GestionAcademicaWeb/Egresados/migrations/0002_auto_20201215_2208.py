# Generated by Django 3.1.1 on 2020-12-16 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Egresados', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusuarios',
            name='email',
            field=models.EmailField(max_length=50, unique=True, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='customusuarios',
            name='matricula',
            field=models.IntegerField(unique=True, verbose_name='Matricula'),
        ),
    ]
