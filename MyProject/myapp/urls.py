from django.urls import path
from myapp.views import *

# Create your views here.

urlpatterns = [
    path("", usuario, name="usuario"),
    path("teste/", index, name="index"),
    path("cadastrar/", cadastrar, name="criar_item"),
    path("editar/<int:id>", editar, name="editar_item"),
    path("atualizar/<int:id>", atualizar, name="atualizar_item"),
    path("visualizar/<int:id>", visualizar, name="visualizar_item"),
    path("visualizar/<int:id>", visualizar, name="comprar_item"),
    path("deletar/<int:id>", deletar, name="deletar_item")
]