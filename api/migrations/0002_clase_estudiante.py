# Generated by Django 4.1.5 on 2023-01-10 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clase',
            name='estudiante',
            field=models.ManyToManyField(to='api.estudiante'),
        ),
    ]
