from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nombre


class Factura(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('pagada', 'Pagada'),
        ('cancelada', 'Cancelada'),
    ]
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    fecha_emision = models.DateField(auto_now_add=True)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)

    def __str__(self):
        return f'Factura {self.id} - {self.estudiante.nombre}'

    @staticmethod
    def generar_reporte_facturas():
        from facturación.models import Factura as FacturaFacturacion
        
        facturas = FacturaFacturacion.objects.all()
        reporte = []

        for factura in facturas:
            reporte.append({
                'id': factura.id,
                'estudiante': factura.estudiante.nombre,
                'estado': factura.estado_actual(),
                'saldo_pendiente': factura.calcular_saldo_pendiente(),
                'monto_total': factura.monto_total,
                'fecha_emision': factura.fecha_emision,
            })

        return reporte
