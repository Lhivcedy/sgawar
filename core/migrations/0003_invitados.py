# Generated by Django 3.2.4 on 2021-07-09 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_usuarios_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invitados',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rut', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=250)),
                ('capacitacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.capacitaciones')),
                ('gerencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.gerencia')),
            ],
        ),
    ]
