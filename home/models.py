from django.db import models


class Auto(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    fecha_creacion = models.DateField(null=True)
    
    def __str__(self):
        return f'{self.marca} - {self.modelo}'