
from django.views.generic import ListView

from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Cotizacion
from .forms import Cotizacion_forms


def home(request):
   
    return HttpResponse("aqui va lo de cotizacion costo valo %utilidad" )


def about(request):
   
    return HttpResponse("aqui sobre nosotros lo que somos" )


class listado(ListView):
    context_object_name = "cotizaciones"
    queryset = Cotizacion.objects.all()
    template_name = "listadocotiza.html"

def store(request):
   
    return HttpResponse("infor  de lugara" )

def contact(request):
   
    return HttpResponse("inf de contactos" )

def blog(request):
    form = Cotizacion_forms(request.POST)
    if form.is_valid():
        form.save
        return redirect('services')
    else:
        form = Cotizacion_forms()
        return render(request,'form_cotizacion.html',{'form': form})