from django.shortcuts import render,get_object_or_404
from .models import Usuario
from Entrega.models import Entrega

def index(request):
    if request.method == 'POST':
        
        cedula = request.POST.get('cedula')
        nombre = request.POST.get('nombre')
        fecha_nacimiento = request.POST.get('fecha_nacimiento')
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')

        miUsuario= Usuario.objects.create(
            cc_usuario=cedula,
            nombre_completo=nombre,
            fecha_nacimiento=fecha_nacimiento,
            direccion=direccion,
            telefono=telefono,
        )


        return render (request, 'Usuarios/index.html', {
        'title' : 'guardo',
    })
    return render (request, 'Usuarios/index.html', {
        'title' : 'Registro de usuario'
    })




def buscar22(request):
    if request.method == 'POST':
        id_escritura = request.POST.get('id_escritura')

        # Verificar si el id_escritura existe en el modelo Entrega relacionado con Usuario
        try:
            usuario_con_entrega = Usuario.objects.get(entrega__id_escritura=id_escritura)
            entrega_existente = usuario_con_entrega.entrega_set.get(id_escritura=id_escritura)
        except Usuario.DoesNotExist:
            entrega_existente = None
        except Entrega.DoesNotExist:
            entrega_existente = None

        return render(request, 'Usuarios/Encontrado.html', {
            'title': 'Detalles de la Entrega Existente',
            'entrega_existente': entrega_existente
        })

    return render(request, 'Usuarios/buscar.html', {'title': 'Registro de entrega'})
