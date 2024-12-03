from django import forms
from .models import Factura, Recibo

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ['estudiante', 'monto_total', 'estado']

class ReciboForm(forms.ModelForm):
    class Meta:
        model = Recibo
        fields = ['fecha_pago', 'monto_pagado']
