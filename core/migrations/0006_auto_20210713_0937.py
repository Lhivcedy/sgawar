# Generated by Django 3.2.4 on 2021-07-13 13:37

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210713_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capacitaciones',
            name='fecha',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='capacitaciones',
            name='fecha_fin',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='capacitaciones',
            name='hora',
            field=models.TimeField(default=datetime.time(9, 37, 2, 381394)),
        ),
    ]