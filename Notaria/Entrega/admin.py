from django.contrib import admin
from .models import Entrega

@admin.register(Entrega)
class EntregaAdmin(admin.ModelAdmin):
    list_display = ('id_entrega', 'id_escritura', 'cc_usuario', 'fecha_entrega')

