from django.shortcuts import render

from django.http import HttpResponse

from django.template import loader

from AppCoder.models import Profesor, Curso


# Create your views here.


def crear_curso(request):
    template=loader.get_template("template2")
    
    clase_1= Curso(nombre="Python", camada="55")
    clase_2= Curso(nombre="C++", camada="50")
    clase_3= Curso(nombre="html", camada="60")
    
    dict_de_curso={
        "clase_1" :clase_1,
        "clase_2" :clase_2,
        "clase_3" :clase_3,
    }

    res = template.render(dict_de_curso)
    
    return HttpResponse(res)


def crear_profesor(request):
    template=loader.get_template("template1.html")
    
        
    profe_1 = Profesor(nombre="Ricardo", apellido="Chumacero",email="ricky@coder.com", profesion="Abogado")
    
    profe_2 = Profesor(nombre="Diego", apellido="Mayo",email="diego@coder.com", profesion="Informatico")
    
    profe_3 = Profesor(nombre="Damian", apellido="Chuma",email="dami@coder.com", profesion="Kioskero")
    
   
    dict_de_contexto= {
        "profe_1" :profe_1,
        "profe_2" :profe_2,
        "profe_3" :profe_3,
    }
   
    res = template.render(dict_de_contexto)
    
    return HttpResponse(res)

