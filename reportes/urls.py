from django.urls import path
from .views import vista_reporte_facturas

urlpatterns = [
    path('reporte-facturas/', vista_reporte_facturas, name='reporte_facturas'),
]
