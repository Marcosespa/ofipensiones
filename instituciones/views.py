from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views import View
from .models import Institucion, Servicio, Curso
from django.forms.models import model_to_dict
import json

class InstitucionListView(View):
    """Vista para listar y crear instituciones."""

    def get(self, request):
        """Lista todas las instituciones."""
        instituciones = Institucion.objects.all()
        data = [model_to_dict(inst) for inst in instituciones]
        return JsonResponse(data, safe=False)

    def post(self, request):
        """Crea una nueva institución."""
        body = json.loads(request.body)
        institucion = Institucion.objects.create(
            nombre=body['nombre'],
            direccion=body['direccion'],
            telefono=body['telefono'],
            email_contacto=body['email_contacto']
        )
        return JsonResponse(model_to_dict(institucion), status=201)


class InstitucionDetailView(View):
    """Vista para consultar y actualizar una institución específica."""

    def get(self, request, pk):
        """Obtiene los detalles de una institución específica."""
        institucion = get_object_or_404(Institucion, pk=pk)
        return JsonResponse(model_to_dict(institucion))

    def put(self, request, pk):
        """Actualiza una institución específica."""
        body = json.loads(request.body)
        institucion = get_object_or_404(Institucion, pk=pk)

        # Actualizar campos
        institucion.nombre = body.get('nombre', institucion.nombre)
        institucion.direccion = body.get('direccion', institucion.direccion)
        institucion.telefono = body.get('telefono', institucion.telefono)
        institucion.email_contacto = body.get('email_contacto', institucion.email_contacto)
        institucion.save()

        return JsonResponse(model_to_dict(institucion))


class ServicioListView(View):
    """Vista para listar y crear servicios para una institución."""

    def get(self, request, institucion_id):
        """Lista los servicios de una institución."""
        institucion = get_object_or_404(Institucion, pk=institucion_id)
        servicios = institucion.servicios.all()
        data = [model_to_dict(serv) for serv in servicios]
        return JsonResponse(data, safe=False)

    def post(self, request, institucion_id):
        """Crea un servicio para una institución específica."""
        body = json.loads(request.body)
        institucion = get_object_or_404(Institucion, pk=institucion_id)
        servicio = Servicio.objects.create(
            institucion=institucion,
            nombre=body['nombre'],
            descripcion=body['descripcion'],
            costo=body['costo']
        )
        return JsonResponse(model_to_dict(servicio), status=201)


class ServicioDetailView(View):
    """Vista para consultar y actualizar un servicio específico."""

    def get(self, request, institucion_id, servicio_id):
        """Obtiene los detalles de un servicio específico."""
        servicio = get_object_or_404(Servicio, pk=servicio_id, institucion_id=institucion_id)
        return JsonResponse(model_to_dict(servicio))

    def put(self, request, institucion_id, servicio_id):
        """Actualiza un servicio específico."""
        body = json.loads(request.body)
        servicio = get_object_or_404(Servicio, pk=servicio_id, institucion_id=institucion_id)

        # Actualizar campos
        servicio.nombre = body.get('nombre', servicio.nombre)
        servicio.descripcion = body.get('descripcion', servicio.descripcion)
        servicio.costo = body.get('costo', servicio.costo)
        servicio.save()

        return JsonResponse(model_to_dict(servicio))


class CursoListView(View):
    """Vista para listar y crear cursos para una institución."""

    def get(self, request, institucion_id):
        """Lista los cursos de una institución."""
        institucion = get_object_or_404(Institucion, pk=institucion_id)
        cursos = institucion.cursos.all()
        data = [model_to_dict(curso) for curso in cursos]
        return JsonResponse(data, safe=False)

    def post(self, request, institucion_id):
        """Crea un curso para una institución específica."""
        body = json.loads(request.body)
        institucion = get_object_or_404(Institucion, pk=institucion_id)
        curso = Curso.objects.create(
            institucion=institucion,
            nombre=body['nombre'],
            descripcion=body['descripcion'],
            duracion_semanas=body['duracion_semanas'],
            fecha_inicio=body['fecha_inicio']
        )
        return JsonResponse(model_to_dict(curso), status=201)


class CursoDetailView(View):
    """Vista para consultar y actualizar un curso específico."""

    def get(self, request, institucion_id, curso_id):
        """Obtiene los detalles de un curso específico."""
        curso = get_object_or_404(Curso, pk=curso_id, institucion_id=institucion_id)
        return JsonResponse(model_to_dict(curso))

    def put(self, request, institucion_id, curso_id):
        """Actualiza un curso específico."""
        body = json.loads(request.body)
        curso = get_object_or_404(Curso, pk=curso_id, institucion_id=institucion_id)

        # Actualizar campos
        curso.nombre = body.get('nombre', curso.nombre)
        curso.descripcion = body.get('descripcion', curso.descripcion)
        curso.duracion_semanas = body.get('duracion_semanas', curso.duracion_semanas)
        curso.fecha_inicio = body.get('fecha_inicio', curso.fecha_inicio)
        curso.save()

        return JsonResponse(model_to_dict(curso))
