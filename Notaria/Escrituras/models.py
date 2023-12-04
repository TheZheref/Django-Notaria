from django.db import models
from Usuarios.models import Usuario  # Importar el modelo Usuario

class Escritura(models.Model):
    id_escritura = models.AutoField(primary_key=True)
    cc_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    acto = models.TextField()
    fecha_escritura = models.DateField()
    

    def __str__(self):
        return f'Escritura {self.id_escritura}'
    
