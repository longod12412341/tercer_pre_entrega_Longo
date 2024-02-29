from django.urls import path
from app_g import views
from app_g.views import *

urlpatterns = [
    path("", inicio, name="inicio"),
    # Vacia, se puede utilizar para la busqueda
    path("cursos/", cursos, name="cursos"), 
    # Vacia hay que empezarla
    path("profesores/", profesFormulario, name="profesFormulario"), 
    # En proceso, no hace nada, pero es para el proyecto
    path("estudiantes/", alumnosFormulario,name="estudiantes" ),
    #Agregar datos a la base de datos de app_g_curso
    path("cursoform", cursoFormulario, name="cursoform"),
    # Buscador de BD
    path("buscar", buscar, name="buscar"),
]

  
  