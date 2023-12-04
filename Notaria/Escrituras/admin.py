
from django.contrib import admin
from .models import Escritura

@admin.register(Escritura)
class EscrituraAdmin(admin.ModelAdmin):
    list_display = ('id_escritura', 'cc_usuario', 'acto', 'fecha_escritura')