from django.urls import path
from .views import crear_factura, listar_facturas, crear_recibo

urlpatterns = [
    path('crear-factura/', crear_factura, name='crear_factura'),
    path('listar-facturas/', listar_facturas, name='listar_facturas'),
    path('crear-recibo/<int:factura_id>/', crear_recibo, name='crear_recibo'),
]
