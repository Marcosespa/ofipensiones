from django.db import models
from datetime import date

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class Factura(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    fecha_emision = models.DateField(auto_now_add=True)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, choices=[
        ('pendiente', 'Pendiente'),
        ('pagada', 'Pagada'),
        ('cancelada', 'Cancelada'),
    ])

    def calcular_saldo_pendiente(self):
        total_pagado = sum(recibo.monto_pagado for recibo in self.recibo_set.all())
        return self.monto_total - total_pagado

    def estado_actual(self):
        saldo_pendiente = self.calcular_saldo_pendiente()
        if saldo_pendiente <= 0:
            return 'Pagada'
        elif self.estado == 'cancelada':
            return 'Cancelada'
        elif date.today() > self.fecha_emision and saldo_pendiente > 0:
            return 'Vencida'
        else:
            return 'Pendiente'

    def __str__(self):
        return f'Factura {self.id} - {self.estudiante.nombre} - Estado Actual: {self.estado_actual()}'

class Recibo(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    fecha_pago = models.DateField()
    monto_pagado = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Recibo {self.id} - Factura {self.factura.id}'
