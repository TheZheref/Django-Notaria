from django.shortcuts import render,redirect
from .models import Escritura
from .models import Usuario



def index(request):
    if request.method == 'POST':
        id_escritura = request.POST['id_escritura']
        cc_usuario = request.POST['cc_usuario']
        acto = request.POST['acto']
        fecha_escritura = request.POST['fecha_escritura']

        # Verificar si el usuario existe
        try:
            usuario = Usuario.objects.get(cc_usuario=cc_usuario)
        except Usuario.DoesNotExist:
            # Si el usuario no existe, mostrar un mensaje y no guardar la escritura
            mensaje_error = "El usuario con la cédula proporcionada no existe."
            return render(request, 'Escrituras/index.html', {'title': 'Usuario no encontrado'})

        # Si el usuario existe, se puede continuar guardando la escritura
        escritura = Escritura(
            id_escritura=id_escritura,
            cc_usuario=usuario,
            acto=acto,
            fecha_escritura=fecha_escritura
        )
        escritura.save()

        # Puedes redirigir a una página de éxito o renderizar una plantilla diferente
        return render(request, 'Escrituras/index.html',{
        'title' : 'Escritura creada'
        })

    return render(request, 'Escrituras/index.html', {
        'title' : 'Registro de Escrituras'
    })