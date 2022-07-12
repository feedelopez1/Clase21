from django.http import HttpResponse
from django.shortcuts import render
from App1.forms import CursoForm

from App1.models import Curso


# Create your views here.

def curso(self):
   curso=Curso(nombre='Django',comision=23312)
   curso.save()
   texto=f'Curso creado: {curso.nombre} {curso.comision}'
   return HttpResponse(texto)

'''def cursoFormulario(request):
   if (request.method=='POST'):
      nombre= request.POST.get('curso')
      comision=request.POST.get('comision')
      curso=Curso(nombre=nombre,comision=comision)
      curso.save()
      return render(request,'App1/inicio.html')


   return render(request, 'App1/cursoFormulario.html')  VISTA PARA FORMUALRIO HTML'''

def cursoFormulario(request):

   if (request.method=='POST'):
      form=CursoForm(request.POST)
      if form.is_valid():
         info= form.cleaned_data
         nombre= info['nombre']
         comision=info['comision']
         curso= Curso(nombre=nombre, comision=comision)
         curso.save()
         return render(request,'App1/inicio.html')      
   else:
      fomr=CursoForm()
      
      return render(request,'App1/cursoFormulario.html',{'form':form})


      return render(request,'App1/inicio.html')

      
   return render(request, 'App1/cursoFormulario.html')

def inicio(request):
   return render(request,'App1/inicio.html')

def cursos(request):
   return render(request,'App1/cursos.html')

def profesores(request):
   return render(request,'App1/profesores.html')

def estudiantes(request):
   return render(request, 'App1/estudiantes.html')

def entregables(request):
   return render(request,'App1/entregables.html')