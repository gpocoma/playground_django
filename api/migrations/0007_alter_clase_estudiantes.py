# Generated by Django 4.1.5 on 2023-01-10 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_clase_table_alter_estudiante_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clase',
            name='estudiantes',
            field=models.ManyToManyField(db_table='tiene', related_name='tiene', to='api.estudiante'),
        ),
    ]
