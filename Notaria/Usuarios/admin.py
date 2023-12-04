from django.contrib import admin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('cc_usuario', 'nombre_completo', 'fecha_nacimiento', 'direccion', 'telefono')

