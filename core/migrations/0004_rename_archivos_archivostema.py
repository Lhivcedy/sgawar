# Generated by Django 3.2.4 on 2021-07-06 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_tema_gerencia'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Archivos',
            new_name='ArchivosTema',
        ),
    ]