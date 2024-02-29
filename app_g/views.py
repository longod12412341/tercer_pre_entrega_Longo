from django.shortcuts import render
from django.http import HttpResponse
from app_g.models import Curso, Estudiante, Profesor
from app_g.forms import cursoform, busca, estudianteform, profesform


# Create your views here.

def inicio(request):
    return render(request, "index.html")

def cursos(request):
    return render(request, "cursos.html")
def profesores(request):
    return render(request, "profesores.html")

def estudiantes(request):
    return render(request, "estudiantes.html")

def alumnosFormulario(request):
 
      if request.method == "POST":
 
            miFormulario = estudianteform(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  
                  informacion = miFormulario.cleaned_data
                  print(f"\n\n\n{miFormulario}")
                  alumno = Estudiante(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"])
                  alumno.save()
                  return render(request, "index.html")
      else:
            miFormulario = estudianteform()
 
      return render(request, "estudiantes.html", {"miformulario": miFormulario})

def profesFormulario(request):
 
      if request.method == "POST":
 
            miFormulario = profesform(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  
                  informacion = miFormulario.cleaned_data
                  print(f"\n\n\n{miFormulario}")
                  profes = Profesor(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"])
                  profes.save()
                  return render(request, "index.html")
      else:
            miFormulario = profesform()
 
      return render(request, "profesores.html", {"miformulario": miFormulario})

def cursoFormulario(request):
 
      if request.method == "POST":
 
            miFormulario = cursoform(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  
                  informacion = miFormulario.cleaned_data
                  print(f"\n\n\n{miFormulario}")
                  curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
                  curso.save()
                  return render(request, "index.html")
      else:
            miFormulario = cursoform()
 
      return render(request, "cursoformulario_01.html", {"miFormulario": miFormulario})





def buscar(request):
    if request.method == "POST":
         miFormulario= busca(request.POST)
         if miFormulario.is_valid():
              info=miFormulario.cleaned_data
              curso = Curso.objects.filter(nombre__icontains=info["nombre"])
              return render(request, "buscar.html", {"cursos":curso})

    else:
         miFormulario = busca()
    return render(request, "buscar.html", {"formulario": miFormulario})
