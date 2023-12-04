from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='Entrega'),
    path('buscar',views.buscar, name='buscar'),
]
