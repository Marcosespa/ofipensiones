from django.shortcuts import render
from .models import Factura

def vista_reporte_facturas(request):
   
    reporte = Factura.generar_reporte_facturas()
    return render(request, 'reporte_facturas.html', {'reporte': reporte})
