from os import name

from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('registrar-cargo', registrar_cargo),
    path('consultar-cargo', consultar_cargo, name='consultar_cargo'),
    path('modificar-cargo/<int:id>', registrar_cargo, name='modificar_cargo'),

]