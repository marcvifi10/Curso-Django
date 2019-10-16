from django.http import HttpResponse
import datetime
from django.template import Template, Context

def saludo(request): # primera vista

    return HttpResponse("<html><body><h1>Hola mundo!!!</h1></body></html>")
    
def despedida(request):

    nombre = "Marc"

    doc_externo = open("E:/Altres arxius/Programació/Django/5 - Plantillas I/Proyecto1/Proyecto1/plantillas/miplantilla.html")

    plt = Template(doc_externo.read())
    
    doc_externo.close()
    
    ctx = Context()
    
    documento = plt.render(ctx)

    return HttpResponse(despedida)
    
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