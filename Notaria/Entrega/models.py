from django.db import models
from Usuarios.models import Usuario  # Importar el modelo Usuario

class Entrega(models.Model):
    id_entrega = models.AutoField(primary_key=True)
    id_escritura = models.ForeignKey('Escrituras.Escritura', on_delete=models.CASCADE)
    cc_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_entrega = models.DateField()

    def __str__(self):
        return f'Entrega {self.id_entrega}'