# Generated by Django 5.1.2 on 2024-11-25 22:06

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_alter_peliculas_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peliculas',
            name='guardado',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]