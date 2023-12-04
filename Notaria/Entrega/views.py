from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Entrega
from Usuarios.models import Usuario
from Escrituras.models import Escritura

def index(request):
    return render (request, 'Entrega/index.html', {
        'title' : 'Registro de entregas'
    })


def index(request):
    if request.method == 'POST':
        id_escritura = request.POST['id_escritura']
        id_usuario = request.POST['cc_usuario']
        fecha_entrega = request.POST['fecha_entrega']

        # Verificar si la escritura existe
        try:
            escritura = Escritura.objects.get(id_escritura=id_escritura)
        except Escritura.DoesNotExist:
            # Si la escritura no existe, mostrar un mensaje y no guardar la entrega
            mensaje_error = "La escritura con el ID proporcionado no existe."
            return render(request, 'Entrega/index.html', {'title': 'Escritura no encontrada'})

        # Verificar si el usuario existe
        try:
            usuario = Usuario.objects.get(cc_usuario=id_usuario)
        except Usuario.DoesNotExist:
            # Si el usuario no existe, mostrar un mensaje y no guardar la entrega
            mensaje_error = "El usuario con la cédula proporcionada no existe."
            return render(request, 'Entrega/index.html', {'title': 'Usuario no encontrado'})

        # Si la escritura y el usuario existen, guardar la entrega
        entrega = Entrega(
            id_escritura=escritura,
            cc_usuario=usuario,
            fecha_entrega=fecha_entrega
        )
        entrega.save()
        

        # Puedes redirigir a una página de éxito o renderizar una plantilla diferente
        return render(request, 'Entrega/index.html', {'title': 'Entrega creada'})

    return render(request, 'Entrega/index.html', {'title': 'Registro de entrega'})



def buscar(request):
    entrega_existente = None

    if request.method == 'POST':
        id_escritura = request.POST.get('id_escritura')

        # Verificar si el id_escritura existe en el modelo Escritura
        try:
            escritura_existente = Escritura.objects.get(id_escritura=id_escritura)
        except Escritura.DoesNotExist:
            escritura_existente = None

        # Ahora puedes utilizar la relación inversa para obtener la Entrega asociada
        if escritura_existente:
            entrega_existente = escritura_existente.entrega_set.first()

        return render(request, 'Entrega/Encontrado.html', {
        'title': 'Detalles de la Entrega Existente',
        'entrega_existente': entrega_existente
        })

    return render(request, 'Entrega/buscar.html', {'title': 'Busqueda de Entregas'})
