from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render

class Persona(object):

    def __init__(self, nombre, apellido):
    
        self.nombre = nombre
        
        self.apellido = apellido

def saludo(request): # primera vista

    return HttpResponse("<html><body><h1>Hola mundo!!!</h1></body></html>")
    
def despedida(request):

    p1 = Persona("Nombre1","Apellido1")

    nombre = "Marc"
    
    apellido = "Villalobos"
    
    ahora = datetime.datetime.now()

    # doc_externo = open("E:/Altres arxius/Programació/Django/5 - Plantillas I/Proyecto1/Proyecto1/plantillas/miplantilla.html")

    # plt = Template(doc_externo.read())
    
    # doc_externo.close()
    
    # doc_externo = loader.get_template('miplantilla.html')
    
    # ctx = Context({"nombre_persona":nombre, "apellido_persona":apellido, "momento_actual":ahora, "nombre_persona2":p1.nombre, "apellido_persona2":p1.apellido})
    
    # documento = doc_externo.render({"nombre_persona":nombre, "apellido_persona":apellido, "momento_actual":ahora, "nombre_persona2":p1.nombre, "apellido_persona2":p1.apellido})

    return render(request, "miplantilla.html", {"nombre_persona":nombre, "apellido_persona":apellido, "momento_actual":ahora, "nombre_persona2":p1.nombre, "apellido_persona2":p1.apellido})
    
def dameFecha(request):

    fecha_actual = datetime.datetime.now()
    
    documento = """
                    <html>
                        <body>
                            <h1>
                                Fecha y hora actual: %s
                            </h1>
                        </body>
                    </html>
                """ % fecha_actual
                
    return HttpResponse(documento)
    
def calculaEdad(request, edad, agno):
    
    periodo = agno-2019
    edadFutura = edad+periodo
    documento = "<html><body>En el año %s tendrás %s años</body></html>" %(agno,edadFutura)
    
    return HttpResponse(documento)