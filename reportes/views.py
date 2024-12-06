from django.shortcuts import render
from .models import Factura

def vista_reporte_facturas(request):
    facturas = Factura.objects.all()
    reporte = [
        {
            'id': factura.id,
            'estudiante': factura.estudiante.nombre,
            'estado': factura.estado_actual(), 
            'saldo_pendiente': factura.calcular_saldo_pendiente(),  
            'monto_total': factura.monto_total,
            'fecha_emision': factura.fecha_emision,
        }
        for factura in facturas
    ]
    return render(request, 'reporte_facturas.html', {'reporte': reporte})
