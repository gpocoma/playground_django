from django.db import models


# Create your models here.
class Estudiante(models.Model):
    id_estudiante = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=256)

    class Meta:
        db_table = 'estudiante'


class Clase(models.Model):
    id_clase = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=256)
    estudiantes = models.ManyToManyField(Estudiante, related_name='tiene', db_table='tiene')

    class Meta:
        db_table = 'clase'
