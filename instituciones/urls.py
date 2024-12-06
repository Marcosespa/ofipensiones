from django.urls import path
from .views import (
    InstitucionListView,
    InstitucionDetailView,
    ServicioListView,
    ServicioDetailView,
    CursoListView,
    CursoDetailView,
)

urlpatterns = [
    # Rutas para Instituciones
    path('instituciones/', InstitucionListView.as_view(), name='instituciones-list'),
    path('instituciones/<int:pk>/', InstitucionDetailView.as_view(), name='instituciones-detail'),

    # Rutas para Servicios
    path('instituciones/<int:institucion_id>/servicios/', ServicioListView.as_view(), name='servicios-list'),
    path('instituciones/<int:institucion_id>/servicios/<int:servicio_id>/', ServicioDetailView.as_view(), name='servicios-detail'),

    # Rutas para Cursos
    path('instituciones/<int:institucion_id>/cursos/', CursoListView.as_view(), name='cursos-list'),
    path('instituciones/<int:institucion_id>/cursos/<int:curso_id>/', CursoDetailView.as_view(), name='cursos-detail'),
]
