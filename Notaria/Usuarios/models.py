from django.db import models


class Usuario(models.Model):
    cc_usuario = models.CharField(max_length=20, primary_key=True)
    nombre_completo = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre_completo
    
   