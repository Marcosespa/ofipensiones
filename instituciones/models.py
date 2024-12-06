from django.db import models

class Institucion(models.Model):
    """Modelo para almacenar información de instituciones vinculadas a OfiPensiones."""
    nombre = models.CharField(max_length=100, unique=True)
    direccion = models.TextField()
    telefono = models.CharField(max_length=15)
    email_contacto = models.EmailField()
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Servicio(models.Model):
    """Modelo para los servicios ofrecidos por una institución."""
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE, related_name="servicios")
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    costo = models.DecimalField(max_digits=10, decimal_places=2)  # Para precios en moneda local.

    def __str__(self):
        return f"{self.nombre} ({self.institucion.nombre})"


class Curso(models.Model):
    """Modelo para los cursos ofrecidos por las instituciones."""
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE, related_name="cursos")
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    duracion_semanas = models.PositiveIntegerField()
    fecha_inicio = models.DateField()

    def __str__(self):
        return f"{self.nombre} - {self.institucion.nombre}"
